import os

my_rules = [
      "C:\\Users\\Hoang Nam\\source\\repos\\WindowsApp22\\WindowsApp22\\obj\\Debug\\WindowsApp22.pdb",
      "cmd.exe /cREG add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\ActiveDesktop /v NoChangingWallPaper /t REG_DWOR",
      "C:\\Users\\file1.txt",
      "C:\\Users\\file2.txt",
      "C:\\Users\\file.txt",
      " /v Wallpaper /t REG_SZ /d %temp%\\IMG.jpg /f",
      " /v DisableAntiSpyware /t REG_DWORD /d 1 /f"
      "All your file has been locked. You must pay money to have a key."
      "After we receive Bitcoin from you. We will send key to your email."
]

def my_rule(my_rules, min_hits=7, max_size_mb=10):
    path = r'C:\Users\Vitalik\PycharmProjects\Programming\PRCT6'
    files = os.listdir(path)

    for file in files:
        file_s = os.path.join(path, file)
        if not os.path.exists(file_s):
            print(" Файл не знайдено.")
            return False

        with open(file_s, "rb") as f:
            content = f.read()

        file_size_mb = os.path.getsize(file_s) / (200 * 1024)
        if file_size_mb > max_size_mb:
            print(f" Файл завеликий ({file_size_mb:.2f} MB) — пропускаємо.")
            return False

        matches = []
        for s in my_rules:
            s_bytes = s.encode()
            if s_bytes in content:
                matches.append(s)

        is_suspicious = len(matches) >= min_hits
        if is_suspicious:
            bad_file = file
            threads = len(matches)

            return bad_file, threads
    return False, 0

suspicious, threads  = my_rule(my_rules)

print(f'Підозрілий файл : {suspicious}, кількість збігів -> {threads}')