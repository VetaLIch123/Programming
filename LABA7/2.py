from colorama import Fore, initЧ
from typing import Tuple

init(autoreset=True)

LOW_CHARS = "abcdefghijklmnopqrstuvwxyz"
UPP_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPC_CHARS = "!@#$%^&*_-"
REQUIRED_LENGTH = 11


def count_char_types(password: str) -> Tuple[int, int, int]:
    low_count = sum(1 for c in password if c in LOW_CHARS)
    upp_count = sum(1 for c in password if c in UPP_CHARS)
    spc_count = sum(1 for c in password if c in SPC_CHARS)
    return low_count, upp_count, spc_count


def max_repeats(password: str, chars: str) -> int:
    max_same = 1
    current = 1
    for i in range(1, len(password)):
        if password[i] in chars and password[i] == password[i - 1]:
            current += 1
            if current > max_same:
                max_same = current
        else:
            current = 1
    return max_same


def only_allowed_chars(password: str) -> bool:
    allowed = set(LOW_CHARS + UPP_CHARS + SPC_CHARS)
    return all(ch in allowed for ch in password)


def validate_password(password: str) -> None:
    low_count, upp_count, spc_count = count_char_types(password)
    same_upp = max_repeats(password, UPP_CHARS)
    same_spc = max_repeats(password, SPC_CHARS)

    cond_length = len(password) >= REQUIRED_LENGTH
    cond_allowed = only_allowed_chars(password)
    cond_low = 3 <= low_count <= 4
    cond_upp = 3 <= upp_count <= 5
    cond_spc = 3 <= spc_count <= 4
    cond_same_upp = same_upp <= 2
    cond_same_spc = same_spc <= 3

    valid = all([cond_length, cond_allowed, cond_low, cond_upp,
                 cond_spc, cond_same_upp, cond_same_spc])

    print()
    print((Fore.GREEN if cond_length else Fore.RED)
          + f"Довжина не менше {REQUIRED_LENGTH} символів – "
          + ("OK!" if cond_length else "FAIL!"))

    print((Fore.GREEN if cond_allowed else Fore.RED)
          + "Пароль містить лише допустимі символи – "
          + ("OK!" if cond_allowed else "FAIL!"))

    print((Fore.GREEN if cond_low else Fore.RED)
          + "Маленькі латинські літери – "
          + ("OK!" if cond_low else "FAIL!"))

    print((Fore.GREEN if cond_upp else Fore.RED)
          + "Великі латинські літери – "
          + ("OK!" if cond_upp else "FAIL!"))

    print((Fore.GREEN if cond_spc else Fore.RED)
          + "Спеціальні символи – "
          + ("OK!" if cond_spc else "FAIL!"))

    print((Fore.GREEN if cond_same_upp else Fore.RED)
          + "Не більше 2 однакових великих літер – "
          + ("OK!" if cond_same_upp else "FAIL!"))

    print((Fore.GREEN if cond_same_spc else Fore.RED)
          + "Не більше 3 однакових спеціальних символів підряд – "
          + ("OK!" if cond_same_spc else "FAIL!"))

    print()
    if valid:
        print(Fore.GREEN + "Пароль валідний!")
    else:
        print(Fore.RED + "Пароль не валідний!")


def main() -> None:
    print(Fore.WHITE + f"Введіть пароль довжиною не менше {REQUIRED_LENGTH} символів.\n"
          "Вимоги до паролю згідно варіанту №20:\n"
          "1. Маленькі літери (3–4)\n"
          "2. Великі літери (3–5)\n"
          "3. Спецсимволи (3–4)\n"
          "4. Не більше 2 однакових великих літер\n"
          "5. Не більше 3 однакових спецсимволів підряд\n")

    password = input(Fore.CYAN + "> ")
    validate_password(password)


if __name__ == "__main__":
    main()
