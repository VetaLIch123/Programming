import requests
from typing import List, Optional


def check_ip_country(ip_list: List[str], token: Optional[str] = None) -> List[Optional[str]]:
    countries: List[Optional[str]] = []
    base_url = "https://ipinfo.io"
    for ip in ip_list:
        try:
            if token:
                url = f"{base_url}/{ip}/json?token={token}"
            else:
                url = f"{base_url}/{ip}/json"
            resp = requests.get(url, timeout=10)
            if resp.status_code != 200:
                countries.append(None)
                continue
            data = resp.json()
            country = data.get("country")
            countries.append(country)
        except Exception:
            countries.append(None)
    return countries


if __name__ == "__main__":
    variant_ips = [
        "62.80.178.146",
        "217.79.179.177",
        "149.202.238.204",
        "37.57.16.5",
        "202.131.229.162"
    ]
    results = check_ip_country(variant_ips, token=None)
    for ip, country in zip(variant_ips, results):
        print(f"{ip} → {country}")
