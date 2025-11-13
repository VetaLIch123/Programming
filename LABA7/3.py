import hashlib
import requests
from typing import Dict, Optional


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


def check_passwords(users_passwords: Dict[str, str]) -> Dict[str, Optional[bool]]:
    results: Dict[str, Optional[bool]] = {}
    for user, password in users_passwords.items():
        result = check_password(password)
        if result == 0:
            results[user] = True
        elif result > 0:
            results[user] = False
        else:
            results[user] = None
    return results


if __name__ == "__main__":
    test_passwords = {
        "user1": "Qwerty123!",
        "user2": "Strong_Pass_999",
        "user3": "password"
    }

    results = check_passwords(test_passwords)
    for user, status in results.items():
        if status is True:
            print(f"{user}: 0")
        elif status is False:
            print(f"{user}: -1")
        else:
            print(f"{user}: -1")
