import json
from typing import Any, Dict, List


def filter_by_ip(logs: List[Dict[str, Any]], suspicious_ip: str) -> List[Dict[str, Any]]:
    return [
        log for log in logs
        if "raddr" in log
           and isinstance(log["raddr"], dict)
           and log["raddr"].get("ip") == suspicious_ip
    ]


def filter_by_port(logs: List[Dict[str, Any]], suspicious_port: int) -> List[Dict[str, Any]]:
    result: List[Dict[str, Any]] = []
    for log in logs:
        for key in ("laddr", "raddr"):
            addr = log.get(key)
            if isinstance(addr, dict) and addr.get("port") == suspicious_port:
                result.append(log)
                break
    return result


def get_suspicious_pids(
        logs: List[Dict[str, Any]],
        suspicious_ip: str,
        suspicious_port: int
) -> List[int]:
    by_ip = {log["pid"] for log in filter_by_ip(logs, suspicious_ip)}
    by_port = {log["pid"] for log in filter_by_port(logs, suspicious_port)}
    return sorted(by_ip & by_port)


def main() -> None:
    with open("system_logs.json", "r", encoding="utf-8") as f:
        logs: List[Dict[str, Any]] = json.load(f)

    suspicious_ip = "192.168.1.1"
    suspicious_port = 80

    pids = get_suspicious_pids(logs, suspicious_ip, suspicious_port)

    if pids:
        print("Підозрілі PID процесів:", *pids)
    else:
        print("Підозрілих процесів не знайдено.")


if __name__ == "__main__":
    main()
