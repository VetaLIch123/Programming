import json
from rich.table import Table
from rich.console import Console

with open("countries_data.json", "r") as f:
    countries = json.load(f)

console = Console()

spanish_countries = [c for c in countries if "Spanish" in c.get("languages", [])]

spanish_sorted = sorted(spanish_countries, key=lambda x: x["population"], reverse=True)

top10_spanish = spanish_sorted[:10]

total_spanish_pop = sum(c["population"] for c in spanish_countries)

english_countries = [c for c in countries if "English" in c.get("languages", [])]

english_sorted = sorted(english_countries, key=lambda x: x["population"])

bottom10_english = english_sorted[:10]

total_english_pop = sum(c["population"] for c in english_countries)

table_spanish = Table(title="10 країн з найбільшим населенням (іспанська мова)")
table_spanish.add_column("№", justify="center")
table_spanish.add_column("Країна")
table_spanish.add_column("Населення", justify="right")
table_spanish.add_column("Мови")
table_spanish.add_column("Валюта")

for i, c in enumerate(top10_spanish, start=1):
    table_spanish.add_row(str(i), c["name"], str(c["population"]),
                          ", ".join(c.get("languages", [])), c.get("currency", "—"))

table_english = Table(title="10 країн з найменшим населенням (англійська мова)")
table_english.add_column("№", justify="center")
table_english.add_column("Країна")
table_english.add_column("Населення", justify="right")
table_english.add_column("Мови")
table_english.add_column("Валюта")

for i, c in enumerate(bottom10_english, start=1):
    table_english.add_row(str(i), c["name"], str(c["population"]),
                          ", ".join(c.get("languages", [])), c.get("currency", "—"))

console.print(table_spanish)
console.print(f"[bold yellow]Сумарна чисельність населення в іспаномовних країнах:[/bold yellow] {total_spanish_pop:,}")

console.print()
console.print(table_english)
console.print(f"[bold yellow]Сумарна чисельність населення в англомовних країнах:[/bold yellow] {total_english_pop:,}")
