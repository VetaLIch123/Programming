from colorama import Fore, init
init(autoreset=True)

leng = 11
upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = "abcdefghijklmnopqrstuvwxyz"
spc = "!@#$%^&*_-"

print(Fore.WHITE + f"Введіть пароль довжиною не менше {leng} символів.\n"
      "Вимоги до паролю:\n"
      "1. Маленькі літери (2–4)\n"
      "2. Великі літери (3–5)\n"
      "3. Спецсимволи (3–4)\n"
      "4. Не більше 2 однакових великих літер\n"
      "5. Не більше 3 однакових спецсимволів підряд\n")

pwd = input(Fore.CYAN + "> ")

low_count = 0
upp_count = 0
spc_count = 0

same_upp = 1
same_spc = 1
max_same_spc = 1

i = 0
while i < len(pwd):
    ch = pwd[i]
    if ch in low:
        low_count += 1
    elif ch in upp:
        upp_count += 1
    elif ch in spc:
        spc_count += 1

    if i > 0:
        prev = pwd[i - 1]
        # для великих літер (правило 26)
        if ch in upp and prev == ch:
            same_upp += 1
        else:
            same_upp = 1

        # для спецсимволів (правило 34)
        if ch in spc and prev == ch:
            same_spc += 1
            if same_spc > max_same_spc:
                max_same_spc = same_spc
        else:
            same_spc = 1
    i += 1

# --- Перевірка правил ---
cond1 = len(pwd) >= leng
cond2 = low_count >= 3 and low_count <= 4
cond3 = upp_count >= 3 and upp_count <= 5
cond4 = spc_count >= 3 and spc_count <= 4
cond5 = same_upp <= 2
cond6 = max_same_spc <= 3

if cond1:
    print(Fore.GREEN + f"Довжина ≥ {leng} символів – OK!")
else:
    print(Fore.RED + f"Довжина ≥ {leng} символів – FAIL!")

if cond2:
    print(Fore.GREEN + "Маленькі літери (3–4) – OK!")
else:
    print(Fore.RED + "Маленькі літери (3–4) – FAIL!")

if cond3:
    print(Fore.GREEN + "Спецсимволи (3-4) - OK!")
else:
    print(Fore.RED + "Спецсимволи (3–4) – FAIL!")

if cond4:
    print(Fore.GREEN + "Не більше 2 однакових великих літер - OK!")
else:
    print(Fore.RED + "Не більше 2 однакових великих літер – FAIL!")

if cond5:
    print(Fore.GREEN + "Не більше 3 однакових спецсимволів підряд - OK!")
else:
    print(Fore.RED + "Не більше 3 однакових спецсимволів підряд – FAIL!")