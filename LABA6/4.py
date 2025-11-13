import csv
from collections import defaultdict
from rich.console import Console
from rich.table import Table

FILENAME = "log_file_20.csv"

console = Console()

fail_counts = defaultdict(int)
ip_users = defaultdict(set)
user_logs = defaultdict(list)
ip_logs = defaultdict(list)

with open(FILENAME, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames if reader.fieldnames else ["user_name", "timestamp", "ip", "logon_status"]

    for row in reader:
        user = row.get("user_name", "").strip()
        ip = row.get("ip", "").strip()
        status = row.get("logon_status", "").strip().lower()

        user_logs[user].append(row)
        ip_logs[ip].append(row)

        if status == "fail":
            fail_counts[user] += 1

        if user:
            ip_users[ip].add(user)

THRESH_USERS = 6
suspicious_users = sorted([u for u, c in fail_counts.items() if c >= THRESH_USERS])

console.print(f"[bold cyan]Користувачі з >= {THRESH_USERS} невдалих спроб (знайдено: {len(suspicious_users)}):[/bold cyan]")
for u in suspicious_users:
    console.print(f" - {u}  (fails = {fail_counts[u]})")

for u in suspicious_users:
    table = Table(title=f"Логи користувача: {u}", show_lines=True)
    for h in headers:
        table.add_column(h, overflow="fold")
    for r in user_logs.get(u, []):
        table.add_row(*(r.get(h, "") for h in headers))
    console.print(table)

THRESH_IPS = 3
suspicious_ips = sorted([ip for ip, users in ip_users.items() if len(users) >= THRESH_IPS])

console.print(f"\n[bold magenta]IP-адреси з входами в >= {THRESH_IPS} різних акаунтів (знайдено: {len(suspicious_ips)}):[/bold magenta]")
for ip in suspicious_ips:
    console.print(f" - {ip}  (distinct users = {len(ip_users[ip])})")

for ip in suspicious_ips:
    table = Table(title=f"Логи з IP: {ip}", show_lines=True)
    for h in headers:
        table.add_column(h, overflow="fold")
    for r in ip_logs.get(ip, []):
        table.add_row(*(r.get(h, "") for h in headers))
    console.print(table)

console.print("\n[bold green]Контрольні підсумки:[/bold green]")
console.print(f"Користувачів з >= {THRESH_USERS} невдалих спроб: {len(suspicious_users)}")
console.print(f"IP-адрес з входами в >= {THRESH_IPS} різних акаунтів: {len(suspicious_ips)}")
