from typing import TypeVar, Any, Sequence, Mapping, Callable, Generator, Literal, Final
# Виправлено арифметику і типи
variable_name: float = 10 / 2

# Було value - "!"*excitement → тепер правильна конкатенація рядків
def fmt(value: str, excitement: int = 10) -> str:
    return value + "!" * excitement

# Було неправильне передавання типів
fmt('Hello', 3)

# None не відповідає анотації int | float, тому використовуємо float | None
my_age: float | None = None
my_city: str | None = None

# Було int | float, а треба TypeAlias
from typing import TypeAlias

number: TypeAlias = float
prices: list[number] = [100, 105, 125.5]

# Image має бути вкладений список
Image = list[list[int]]
image: Image = [[i for i in range(10)] for _ in range(10)]

# TypeVar повинен використовуватись правильно
T1 = TypeVar('T1')
DictWithIntKey = dict[int, T1]

a: DictWithIntKey[str] = {0: 'zero', 1: 'one'}
b: DictWithIntKey[bool] = {0: False, 1: True}
c: DictWithIntKey[int] = {0: 0, 1: 1}
d: DictWithIntKey[float] = {0: 0.0, 1: 1.0}

T2 = TypeVar('T2')

def combine(a: T2, b: T2) -> str:
    return str(a) + str(b)

print(combine(10, 20))
print(combine('hello', 'world'))
print(combine('hello', 'word'))

lst_1: list[int | str] = [1, "2"]
lst_2: list[int] = [1, 2, 3, 4]
lst_3: list[list[int]] = [[1, 2], [3, 4]]

tpl_1: tuple[int, ...] = (1, 2, 3, 4)
tpl_2: tuple[list[int], list[str]] = ([1, 2], ['1', '2'])
tpl_3: tuple[list[int], list[int], list[int]] = ([1, 2], [3, 4], [5, 6])
tpl_4: tuple[int, ...] = (1, 2, 3, 4)

dt_1: dict[str, int] = {"a": 1, "b": 2}

st_1: set[int | str] = {1, 2, '3', '4'}

def get_first(items: list[Any]) -> Any:
    return items[0]

get_first(['1', 1])

def first_element(items: Sequence[Any]) -> Any:
    return items[0]

first_element((1, 2, 3))

def get_value(data: Mapping[str, Any], key: str) -> Any:
    return data.get(key)

get_value({'1': 2.0, '3': 4.0}, key='1')

def is_twice_as_big(num1: int, num2: int) -> bool:
    return num1 >= 2 * num2

def compare_nums(num1: int, num2: int, comp: Callable[[int, int], bool]) -> int:
    if comp(num1, num2):
        return num1
    else:
        return num2

compare_nums(10, 3, is_twice_as_big)

def do_twice() -> Generator[int, None, None]:
    yield 1
    yield 2

def play(player_name: str):
    print(f"Хід {player_name}")

ret_val = play("Іван")

def calc_div(a: int, b: int) -> float:
    return a / b

ReadOnlyMode = Literal["r", "r+"]

def read_file(file_name: str, mode: ReadOnlyMode) -> None:
    pass

read_file('data.txt', 'r')
MAX_SIZE: Final[int] = 1_000
# Видаляємо зміну константи (не можна змінювати Final)