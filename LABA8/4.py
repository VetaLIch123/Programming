import re, os, zipfile, tempfile, shutil, time, urllib.request, argparse
from typing import List, Tuple, Optional

ZIP_NAME = "malware.zip"
ZIP_PWD = "z9$R1fGb"
RULE_FILE = "rule.yar"
GITHUB_RAW = "https://raw.githubusercontent.com/Yara-Rules/rules/master/malware/RANSOM_screenlocker_5h311_1nj3c706.yar"
RE_LINE = re.compile(r'^\s*(\$\w+)\s*=\s*(?P<pat>"(?:\\.|[^"])*"|\{[0-9A-Fa-f\s\?]+\})\s*(?P<mods>.*)$')

def load_rule(path: str) -> Optional[str]:
    if os.path.exists(path):
        return open(path, "r", encoding="utf-8", errors="ignore").read()
    try:
        with urllib.request.urlopen(GITHUB_RAW, timeout=8) as r:
            return r.read().decode("utf-8", errors="ignore")
    except Exception:
        return None

def parse_plain_signatures(text: str) -> List[Tuple[str, bytes, bool]]:
    out = []
    m = re.search(r"strings\s*:\s*(.*?)\n\s*condition\s*:", text, re.S | re.I)
    block = m.group(1) if m else text
    for ln in block.splitlines():
        lm = RE_LINE.match(ln)
        if not lm:
            continue
        ident = lm.group(1)
        pat = lm.group('pat').strip()
        mods = lm.group('mods') or ""
        nocase = bool(re.search(r"\bnocase\b", mods, re.I))
        if pat.startswith('"') and pat.endswith('"'):
            inner = pat[1:-1]
            try:
                decoded = bytes(inner, "utf-8").decode("unicode_escape").encode("utf-8")
            except Exception:
                decoded = inner.encode("utf-8", errors="ignore")
            out.append((ident, decoded, nocase))
        elif pat.startswith("{") and pat.endswith("}"):
            body = pat[1:-1].strip()
            if "?" in body:
                continue
            parts = [p for p in body.split() if p]
            try:
                b = bytes(int(p, 16) for p in parts)
                out.append((ident, b, False))
            except Exception:
                continue
    return out

def extract_zip(zip_path: str, pwd: str) -> Optional[str]:
    if not os.path.exists(zip_path):
        print(f"Архів '{zip_path}' не знайдено.")
        return None
    tmp = tempfile.mkdtemp(prefix="yara_tmp_")
    try:
        with zipfile.ZipFile(zip_path) as z:
            z.extractall(path=tmp, pwd=pwd.encode())
        return tmp
    except RuntimeError:
        print("Помилка: можливо, неправильний пароль для архіву.")
    except zipfile.BadZipFile:
        print("Помилка: архів пошкоджено або не є ZIP.")
    except Exception as e:
        print("Помилка при розпаковці:", e)
    shutil.rmtree(tmp, ignore_errors=True)
    return None

def scan_folder(folder: str, patterns: List[Tuple[str, bytes, bool]]) -> dict:
    matches = {}
    for root, _, files in os.walk(folder):
        for fn in files:
            p = os.path.join(root, fn)
            try:
                data = open(p, "rb").read()
            except Exception:
                continue
            found = []
            lower = data.lower()
            for ident, pat, nocase in patterns:
                if nocase:
                    if pat.lower() in lower:
                        found.append(ident)
                else:
                    if pat in data:
                        found.append(ident)
            if found:
                matches[os.path.relpath(p, folder)] = found
    return matches

def main():
    ap = argparse.ArgumentParser(description="Компактний YARA-like сканер з ZIP.")
    ap.add_argument("--zip", "-z", default=ZIP_NAME)
    ap.add_argument("--pwd", "-p", default=ZIP_PWD)
    ap.add_argument("--rule", "-r", default=RULE_FILE)
    ap.add_argument("--keep", action="store_true", help="Не видаляти тимчасову теку після сканування")
    args = ap.parse_args()

    print("Завантажую правило...")
    rule_text = load_rule(args.rule)
    if not rule_text:
        print("Не вдалося завантажити правило локально або з GitHub.")
        return

    patterns = parse_plain_signatures(rule_text)
    if not patterns:
        print("У правилі не знайдено простих сигнатур для пошуку.")
        return
    print(f"Підготовлено {len(patterns)} сигнатур (текст/hex без wildcard).")

    tmp = extract_zip(args.zip, args.pwd)
    if not tmp:
        return
    print(f"Розпаковано у: {tmp}\nСканую файли...")
    t0 = time.time()
    matches = scan_folder(tmp, patterns)
    dt = time.time() - t0

    if matches:
        print("\nЗнайдені сигнатури у файлах:")
        for fn, ids in matches.items():
            print(f" - {fn}: {', '.join(ids)}")
    else:
        print("\nСигнатури не знайдені.")
    print(f"\nЧас: {dt:.2f} с")

    if args.keep:
        print("Тека залишена:", tmp)
    else:
        shutil.rmtree(tmp, ignore_errors=True)
        print("Тимчасова тека видалена.")

if __name__ == "__main__":
    main()
