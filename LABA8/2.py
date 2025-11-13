import json
from typing import List, Dict, Any, Optional

City = Dict[str, Any]
DB_FILE = "cities_db.json"

DEFAULT_CITIES: List[City] = [
    {"name": "Львів", "country": "Україна", "population": 717510, "founded": 1256, "area": 182.0},
    {"name": "Київ", "country": "Україна", "population": 2967000, "founded": 482, "area": 839.0},
    {"name": "Варшава", "country": "Польща", "population": 1790658, "founded": 1300, "area": 517.2},
    {"name": "Прага", "country": "Чехія", "population": 1335000, "founded": 880, "area": 496.0},
    {"name": "Берлін", "country": "Німеччина", "population": 3645000, "founded": 1237, "area": 891.8},
]


def load_db() -> List[City]:
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                print("Базу даних успішно завантажено з файлу.")
                return data
            else:
                print("Помилка: файл має неправильний формат — очікувався список. Створюю порожню базу.")
                return []
    except FileNotFoundError:
        print("Файл бази даних не знайдено. Буде використано початковий набір міст.")
        return []
    except json.JSONDecodeError:
        print("Помилка читання JSON (файл пошкоджено). Створюю порожню базу.")
        return []
    except Exception as e:
        print(f"Несподівана помилка при завантаженні файлу: {e}")
        return []


def save_db(cities: List[City]) -> None:
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(cities, f, ensure_ascii=False, indent=4)
        print("Базу даних збережено у файл.")
    except Exception as e:
        print(f"Помилка збереження: {e}")


def show_all(cities: List[City]) -> None:
    if not cities:
        print("База даних порожня.")
        return
    print("\n--- Всі міста в базі ---")
    for i, city in enumerate(cities):
        print(f"{i}: Назва: {city.get('name', 'N/A')}, Країна: {city.get('country', 'N/A')}, "
              f"Населення: {city.get('population', 'N/A')}, Засновано: {city.get('founded', 'N/A')}, "
              f"Площа: {city.get('area', 'N/A')} км²")


def add_city(cities: List[City]) -> None:
    name = input("Назва міста: ").strip()
    country = input("Країна: ").strip()
    try:
        population = int(input("Населення: ").strip())
        founded = int(input("Рік заснування: ").strip())
        area = float(input("Площа (км²): ").strip())
    except ValueError:
        print("Помилка: введено неправильний тип даних. Місто не додано.")
        return

    city = {
        "name": name,
        "country": country,
        "population": population,
        "founded": founded,
        "area": area,
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
    try:
        cities.sort(key=lambda x: x.get(attribute, 0))
        print(f"Відсортовано за атрибутом '{attribute}'.")
    except Exception as e:
        print(f"Помилка сортування: {e}")


def delete_by_attribute(cities: List[City], attribute: str, value: Any) -> None:
    before = len(cities)
    cities[:] = [city for city in cities if str(city.get(attribute)) != str(value)]
    after = len(cities)
    print(f"Видалено {before - after} запис(ів).")


def delete_by_index(cities: List[City], index: int) -> None:
    try:
        removed = cities.pop(index)
        print(f"Видалено запис: {removed}")
    except IndexError:
        print("Помилка: невірний індекс.")


def filter_by_attribute(cities: List[City], attribute: str, value: Any) -> List[City]:
    return [city for city in cities if str(city.get(attribute)) == str(value)]


def main() -> None:
    loaded = load_db()

    if not loaded:
        cities: List[City] = DEFAULT_CITIES.copy()
        print("Завантажено початковий набір міст.")
    else:
        cities = loaded

    while True:
        print("\n--- Меню ---")
        print("1. Вивести всі міста")
        print("2. Додати місто")
        print("3. Сортувати за атрибутом")
        print("4. Видалити за атрибутом")
        print("5. Видалити за індексом")
        print("6. Вивести всі елементи за атрибутом")
        print("7. Зберегти БД у файл")
        print("8. Завантажити БД з файлу")
        print("0. Вийти")
        choice = input("Ваш вибір: ").strip()
        if choice == "1":
            show_all(cities)
        elif choice == "2":
            add_city(cities)
        elif choice == "3":
            attr = input("Вкажіть атрибут для сортування (name/country/population/founded/area): ").strip()
            sort_by_attribute(cities, attr)
        elif choice == "4":
            attr = input("Атрибут для видалення: ").strip()
            val = input("Значення: ").strip()
            delete_by_attribute(cities, attr, val)
        elif choice == "5":
            try:
                idx = int(input("Індекс для видалення: ").strip())
                delete_by_index(cities, idx)
            except ValueError:
                print("Помилка: потрібно ввести число.")
        elif choice == "6":
            attr = input("Атрибут: ").strip()
            val = input("Значення: ").strip()
            found = filter_by_attribute(cities, attr, val)
            if found:
                for c in found:
                    print(c)
            else:
                print("Нічого не знайдено.")
        elif choice == "7":
            save_db(cities)
        elif choice == "8":
            loaded_again = load_db()
            if loaded_again:
                cities = loaded_again
                print("БД перезавантажено з файлу.")
            else:
                print("Файл або порожній, або пошкоджений; залишився поточний набір у пам'яті.")
        elif choice == "0":
            print("Вихід із програми.")
            break
        else:
            print("Невірний вибір.")
if __name__ == "__main__":
    main()
