from rich.console import Console
from rich.table import Table

console = Console()

cities = [
    ["Київ", "Україна", 2884000, 482, 847.66],
    ["Львів", "Україна", 721000, 1256, 182.0],
    ["Харків", "Україна", 1441000, 1654, 350.0],
    ["Одеса", "Україна", 1008000, 1415, 236.9],
    ["Дніпро", "Україна", 964000, 1776, 405.0],
]

def show_table(data, title="База даних міст"):
    table = Table(title=title, show_lines=True)
    table.add_column("№")
    headers = ["Назва", "Країна", "Населення", "Рік", "Площа (км²)"]
    for h in headers:
        table.add_column(h, justify="left")
    for i, row in enumerate(data, 1):
        table.add_row(str(i), *map(str, row))
    console.print(table)

while True:
    print("\nМеню:")
    print("1 - Вивести весь список")
    print("2 - Додати елемент")
    print("3 - Сортувати за атрибутом")
    print("4 - Видалити за атрибутом")
    print("5 - Видалити за індексом")
    print("6 - Вивести за атрибутом")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        show_table(cities)

    elif choice == "2":
        name = input("Назва міста: ")
        country = input("Країна: ")
        population = int(input("Населення: "))
        year = int(input("Рік заснування: "))
        area = float(input("Площа: "))
        cities.append([name, country, population, year, area])
        console.print("[green]Місто додано![/green]")

    elif choice == "3":
        print("1-Назва, 2-Країна, 3-Населення, 4-Рік, 5-Площа")
        k = int(input("Сортувати за номером атрибуту: ")) - 1
        cities.sort(key=lambda x: x[k])
        console.print("[yellow]Список відсортовано![/yellow]")

    elif choice == "4":
        attr = input("Введіть назву міста для видалення: ")
        cities = [c for c in cities if c[0] != attr]
        console.print("[red]Місто видалено (якщо було знайдено)![/red]")

    elif choice == "5":
        idx = int(input("Введіть індекс (з 1): ")) - 1
        if 0 <= idx < len(cities):
            del cities[idx]
            console.print("[red]Рядок видалено![/red]")
        else:
            console.print("[red]Невірний індекс![/red]")

    elif choice == "6":
        country = input("Введіть країну: ")
        filtered = [c for c in cities if c[1] == country]
        show_table(filtered, f"Міста країни {country}")

    elif choice == "0":
        break

    else:
        console.print("[red]Невірний вибір![/red]")
