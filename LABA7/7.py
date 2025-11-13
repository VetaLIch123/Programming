from typing import List, Dict, Any

City = Dict[str, Any]


def show_all(cities: List[City]) -> None:
    if not cities:
        print("База даних порожня.")
        return
    for i, city in enumerate(cities):
        print(f"{i}: {city}")


def add_city(cities: List[City]) -> None:
    name = input("Назва міста: ")
    country = input("Країна: ")
    try:
        population = int(input("Населення: "))
        founded = int(input("Рік заснування: "))
        area = float(input("Площа (км²): "))
    except ValueError:
        print("Помилка: введено неправильний тип даних.")
        return

    city = {
        "Назва": name,
        "Країна": country,
        "Популяція": population,
        "Засновано в": founded,
        "Площа": area,
    }
    cities.append(city)
    print("Місто додано.")


def sort_by_attribute(cities: List[City], attribute: str) -> None:
    if not cities:
        print("База порожня.")
        return
    if attribute not in cities[0]:
        print(f"Невідомий атрибут: {attribute}")
        return
    cities.sort(key=lambda x: x[attribute])
    print(f"Відсортовано за атрибутом '{attribute}'.")


def delete_by_attribute(cities: List[City], attribute: str, value: Any) -> None:
    before = len(cities)
    cities[:] = [city for city in cities if city.get(attribute) != value]
    after = len(cities)
    print(f"Видалено {before - after} запис(ів).")


def delete_by_index(cities: List[City], index: int) -> None:
    if 0 <= index < len(cities):
        removed = cities.pop(index)
        print(f"Видалено запис: {removed}")
    else:
        print("Невірний індекс.")


def filter_by_attribute(cities: List[City], attribute: str, value: Any) -> List[City]:
    return [city for city in cities if city.get(attribute) == value]


def main() -> None:
    cities: List[City] = [
        {"name": "Львів", "country": "Україна", "population": 717510, "founded": 1256, "area": 182.0},
        {"name": "Київ", "country": "Україна", "population": 2967000, "founded": 482, "area": 839.0},
        {"name": "Варшава", "country": "Польща", "population": 1790658, "founded": 1300, "area": 517.2},
        {"name": "Прага", "country": "Чехія", "population": 1335000, "founded": 880, "area": 496.0},
        {"name": "Берлін", "country": "Німеччина", "population": 3645000, "founded": 1237, "area": 891.8},
    ]

    while True:
        print("\n--- Меню ---")
        print("1. Вивести всі міста")
        print("2. Додати місто")
        print("3. Сортувати за атрибутом")
        print("4. Видалити за атрибутом")
        print("5. Видалити за індексом")
        print("6. Вивести всі елементи за атрибутом")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_all(cities)
        elif choice == "2":
            add_city(cities)
        elif choice == "3":
            attr = input("Вкажіть атрибут для сортування: ")
            sort_by_attribute(cities, attr)
        elif choice == "4":
            attr = input("Атрибут для видалення: ")
            val = input("Значення: ")
            delete_by_attribute(cities, attr, val)
        elif choice == "5":
            try:
                idx = int(input("Індекс для видалення: "))
                delete_by_index(cities, idx)
            except ValueError:
                print("Помилка: потрібно ввести число.")
        elif choice == "6":
            attr = input("Атрибут: ")
            val = input("Значення: ")
            found = filter_by_attribute(cities, attr, val)
            if found:
                for c in found:
                    print(c)
            else:
                print("Нічого не знайдено.")
        elif choice == "0":
            print("Вихід із програми.")
            break
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    main()
