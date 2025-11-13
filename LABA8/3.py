import zipfile
import string
import os
import time
from typing import Optional

ZIP_NAME = "Variant 20.zip"
DICT_NAME = "10-million-password-list-top-100000.txt"
ALLOWED = set(string.ascii_lowercase + string.digits)  # a-z0-9

def try_password(zf: zipfile.ZipFile, pwd: str) -> bool:
    try:
        first = zf.namelist()[0]
    except IndexError:
        print("Архів порожній.")
        return False

    try:
        zf.read(first, pwd=pwd.encode('utf-8'))
        return True
    except RuntimeError:
        return False
    except zipfile.BadZipFile:
        print("Помилка: файл не є коректним ZIP-архівом.")
        raise
    except Exception as e:
        print(f"Несподівана помилка при перевірці пароля '{pwd}': {e}")
        return False

def dictionary_attack(zip_path: str, dict_path: str) -> Optional[str]:
    if not os.path.exists(zip_path):
        print(f"Архів '{zip_path}' не знайдено у поточній теці.")
        return None
    if not os.path.exists(dict_path):
        print(f"Файл словника '{dict_path}' не знайдено у поточній теці.")
        return None

    try:
        with zipfile.ZipFile(zip_path) as zf:
            print("Починаю словникову атаку...")
            start = time.time()
            with open(dict_path, "r", encoding="utf-8", errors="ignore") as f:
                for ln, line in enumerate(f, 1):
                    pw = line.strip()
                    if len(pw) != 4:
                        continue
                    if not set(pw).issubset(ALLOWED):
                        continue
                    if try_password(zf, pw):
                        elapsed = time.time() - start
                        print(f"\n[ЗНАЙДЕНО] Пароль: '{pw}' (рядок #{ln} словника). Час: {elapsed:.2f} с")
                        return pw
                    if ln % 20000 == 0:
                        print(f"Прогрес: перевірено {ln} рядків словника...")
            print("Словникова атака завершена — пароль не знайдено у словнику.")
            return None
    except zipfile.BadZipFile:
        print("Неможливо відкрити ZIP (пошкоджено).")
        return None

def extract_and_show(zip_path: str, password: str) -> None:
    dest = f"extracted_{password}"
    os.makedirs(dest, exist_ok=True)
    try:
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(path=dest, pwd=password.encode('utf-8'))
        print(f"Архів розпаковано у папку: {dest}")
    except RuntimeError:
        print("Помилка: невірний пароль при спробі розпакувати.")
        return
    except Exception as e:
        print(f"Помилка при розпакуванні: {e}")
        return
    print("\n-- Вміст розархівованих файлів (текстові файли виводяться частково) --")
    for root, _, files in os.walk(dest):
        for fname in files:
            fpath = os.path.join(root, fname)
            try:
                size = os.path.getsize(fpath)
            except OSError:
                size = -1
            text_exts = (".txt", ".csv", ".py", ".md", ".json", ".xml", ".html", ".htm", ".log")
            print(f"\nФайл: {os.path.relpath(fpath)}  ({size} bytes)")
            if fname.lower().endswith(text_exts) or size <= 10_000:
                try:
                    with open(fpath, "rb") as fh:
                        raw = fh.read(10_000)  # читаємо до 10KB
                    text = raw.decode("utf-8")
                    print("----- Початок файлу (до 10KB) -----")
                    print(text)
                    print("----- Кінець виводу файлу -----")
                except UnicodeDecodeError:
                    print("(Не текстовий файл або не в UTF-8 — пропускаю вивід.)")
                except Exception as e:
                    print(f"(Помилка читання файлу: {e})")
            else:
                print("(Великий або бінарний файл — не виводиться)")

def main():
    print("=== Словникова атака для Variant 20.zip ===")
    ans = input("Підтверджуєш, що маєш право працювати з архівом? (так/ні): ").strip().lower()
    if ans not in ("так", "t", "y", "yes"):
        print("Операцію скасовано.")
        return

    pw = dictionary_attack(ZIP_NAME, DICT_NAME)
    if pw:
        extract_and_show(ZIP_NAME, pw)
        return

    ans2 = input("Словник не допоміг. Спробувати брутфорс по a-z0-9 (36^4 ≈ 1.68M)? (так/ні): ").strip().lower()
    if ans2 not in ("так", "t", "y", "yes"):
        print("Завершення.")
        return

    import itertools
    chars = string.ascii_lowercase + string.digits
    total = len(chars) ** 4
    checked = 0
    start_time = time.time()
    try:
        with zipfile.ZipFile(ZIP_NAME) as zf:
            for combo in itertools.product(chars, repeat=4):
                pw_try = ''.join(combo)
                checked += 1
                if try_password(zf, pw_try):
                    elapsed = time.time() - start_time
                    print(f"\n[ЗНАЙДЕНО брутфорсом] Пароль: '{pw_try}' (перевірено {checked}/{total}). Час: {elapsed:.2f} с")
                    extract_and_show(ZIP_NAME, pw_try)
                    return
                if checked % 100000 == 0:
                    print(f"Перевірено {checked}/{total} паролів...")
    except zipfile.BadZipFile:
        print("Помилка: ZIP пошкоджено.")
        return
    except KeyboardInterrupt:
        print("Брутфорс перервано користувачем.")
        return

    print("Пароль не знайдено навіть брутфорсом.")

if __name__ == "__main__":
    main()
