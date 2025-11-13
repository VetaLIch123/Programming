import csv
from rich.console import Console
from rich.table import Table

console = Console()

with open("Fortune 500 Companies_2023.csv", newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    f500_tbl = list(reader)

headers = f500_tbl[0]
data = f500_tbl[1:]

min_emp = sorted(data, key=lambda r: int(r[7]))[:10]

table = Table(title="10 компаній з найменшою кількістю працівників", show_lines=True)
for h in headers:
    table.add_column(h, justify="left")
for row in min_emp:
    table.add_row(*row)
console.print(table)

ratio = sorted(data, key=lambda r: (int(r[4]) / int(r[6])) if int(r[6]) > 0 else 0, reverse=True)[:10]

table2 = Table(title="10 компаній з найкращим співвідношенням дохід/активи", show_lines=True)
for h in headers:
    table2.add_column(h, justify="left")
for row in ratio:
    table2.add_row(*row)
console.print(table2)
