import hashlib
import requests
from typing import Dict, Generator


def check_password(password: str) -> int:
    try:
        sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return -1

        hashes = (line.split(":") for line in response.text.splitlines())
        for suf, count in hashes:
            if suf == suffix:
                return int(count)
        return 0
    except Exception:
        return -1


def check_passwords_gen(users_passwords: Dict[str, str]) -> Generator[str, None, None]:
    for user, password in users_passwords.items():
        result = check_password(password)
        if result == 0:
            yield user


if __name__ == "__main__":
    test_passwords = {
        "user1": "Qwerty123!",
        "user2": "Strong_Pass_999",
        "user3": "password",
        "user4": "MyUniq-Pass!"
    }

    print("Користувачі з безпечними паролями:")
    for safe_user in check_passwords_gen(test_passwords):
        print(safe_user)
