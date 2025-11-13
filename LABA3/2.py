from colorama import Fore, init
init(autoreset=True)

leng = 11
upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ, АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
low = "abcdefghijklmnopqrstuvwxyz, абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
spc = "!@#$%^&*_-"

print(Fore.WHITE + f"Введіть пароль довжиною не менше {leng} символів.\n"
      "Вимоги до паролю:\n"
      "1. Маленькі літери\n"
      "2. Великі літери\n"
      "3. Спеціальні символи !@#$%^&*_-\n")

pwd = input(Fore.CYAN + "> ")

conds = [
    (len(pwd) >= leng, f"Довжина ≥ {leng} символів"),
    (any(c in low for c in pwd), "Маленькі літери"),
    (any(c in upp for c in pwd), "Великі літери"),
    (any(c in spc for c in pwd), "Спеціальні символи"),
]

for ok, text in conds:
    print((Fore.GREEN + f"{text} – OK!") * ok or (Fore.RED + f"{text} – FAIL!"))

print()
print((Fore.GREEN + "Пароль валідний!") * all(i[0] for i in conds)
      or (Fore.RED + "Пароль не валідний!"))
