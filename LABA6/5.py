from rich.console import Console
from rich.table import Table

console = Console()

cities = [
    {"Назва": "Київ", "Країна": "Україна", "Населення": 2884000, "Рік заснування": 482, "Площа": 847.66},
    {"Назва": "Львів", "Країна": "Україна", "Населення": 721000, "Рік заснування": 1256, "Площа": 182.0},
    {"Назва": "Харків", "Країна": "Україна", "Населення": 1441000, "Рік заснування": 1654, "Площа": 350.0},
    {"Назва": "Одеса", "Країна": "Україна", "Населення": 1008000, "Рік заснування": 1415, "Площа": 236.9},
    {"Назва": "Дніпро", "Країна": "Україна", "Населення": 964000, "Рік заснування": 1776, "Площа": 405.0},
]

while True:
    print("\nМеню:")
    print("1 - Вивести весь список")
    print("2 - Додати елемент")
    print("3 - Сортувати за атрибутом")
    print("4 - Видалити за атрибутом")
    print("5 - Видалити за індексом")
    print("6 - Вивести за атрибутом (фільтр)")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")
    if choice == "1":
        table = Table(title="База даних міст", show_lines=True)
        table.add_column("№")
        for key in cities[0].keys():
            table.add_column(key)

        for i, city in enumerate(cities, 1):
            table.add_row(str(i), city["Назва"], city["Країна"],
                          str(city["Населення"]), str(city["Рік заснування"]), str(city["Площа"]))
        console.print(table)
    elif choice == "2":
        name = input("Назва міста: ")
        country = input("Країна: ")
        population = int(input("Населення: "))
        year = int(input("Рік заснування: "))
        area = float(input("Площа (км²): "))

        cities.append({
            "Назва": name,
            "Країна": country,
            "Населення": population,
            "Рік заснування": year,
            "Площа": area
        })
        console.print("[green]Місто успішно додано![/green]")
    elif choice == "3":
        print("Доступні атрибути: Назва, Країна, Населення, Рік заснування, Площа")
        key = input("Введіть атрибут для сортування: ").capitalize()
        key = "Рік заснування" if key == "Рік" else key
        if key in cities[0]:
            cities.sort(key=lambda x: x[key])
            console.print(f"[yellow]Відсортовано за атрибутом: {key}[/yellow]")
        else:
            console.print("[red]Невірний атрибут![/red]")
    elif choice == "4":
        attr = input("Введіть назву міста для видалення: ")
        found = False
        for city in cities[:]:
            if city["Назва"].lower() == attr.lower():
                cities.remove(city)
                found = True
        if found:
            console.print("[red]Місто видалено![/red]")
        else:
            console.print("[red]Місто не знайдено![/red]")
    elif choice == "5":
        idx = int(input("Введіть індекс (з 1): ")) - 1
        if 0 <= idx < len(cities):
            del cities[idx]
            console.print("[red]Рядок видалено![/red]")
        else:
            console.print("[red]Невірний індекс![/red]")
    elif choice == "6":
        country = input("Введіть країну: ")
        filtered = [c for c in cities if c["Країна"].lower() == country.lower()]
        if filtered:
            table = Table(title=f"Міста країни {country}", show_lines=True)
            table.add_column("№")
            for key in filtered[0].keys():
                table.add_column(key)
            for i, city in enumerate(filtered, 1):
                table.add_row(str(i), city["Назва"], city["Країна"],
                              str(city["Населення"]), str(city["Рік заснування"]), str(city["Площа"]))
            console.print(table)
        else:
            console.print("[red]Міста не знайдено![/red]")
    elif choice == "0":
        console.print("[bold green]Програма завершена.[/bold green]")
        break

    else:
        console.print("[red]Невірний вибір![/red]")
