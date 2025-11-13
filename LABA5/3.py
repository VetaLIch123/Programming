import csv
from rich.console import Console
from rich.table import Table

console = Console()

with open("log_file_20.csv", newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    logs = list(reader)

headers = logs[0]
logs = logs[1:]

users = {}
for row in logs:
    user, _, _, status = row
    if status == "fail":
        users[user] = users.get(user, 0) + 1

suspicious_users = [u for u, c in users.items() if c >= 6]

for u in suspicious_users:
    table = Table(title=f"Логи користувача: {u}", show_lines=True)
    for h in headers:
        table.add_column(h)
    for r in logs:
        if r[0] == u:
            table.add_row(*r)
    console.print(table)

ips = {}
for row in logs:
    user, _, ip, _ = row
    ips.setdefault(ip, set()).add(user)

suspicious_ips = [ip for ip, users in ips.items() if len(users) >= 3]

for ip in suspicious_ips:
    table = Table(title=f"Логи з IP: {ip}", show_lines=True)
    for h in headers:
        table.add_column(h)
    for r in logs:
        if r[2] == ip:
            table.add_row(*r)
    console.print(table)
