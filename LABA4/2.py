quest1 = "Столиця України"
answers1 = [
    "1. Варшава",
    "2. Рим",
    "3. Київ",
    "4. Берлін"
]
correct1 = 3

quest2 = "Що ми вивчаємо"
answers2 = [
    "1. Щось",
    "2. Програмування",
    "3. Математику",
    "4. Не знаю",
]
correct2 = 2

while True:
    print(quest1)
    for answer in answers1:
        print(answer)
    try:
        choice = int(input("Введіть номер правильної відповіді (1–4): "))
        if 1 <= choice <= 4:
            if choice == correct1:
                print("Правильно!")
            else:
                print("Неправильно.")
            break
        else:
            print("Недопустиме значення. Спробуйте ще раз.")
    except ValueError:
        print("Введіть число від 1 до 4.")
while True:
    print(quest2)
    for answer in answers2:
        print(answer)
    try:
        choice = int(input("Введіть номер правильної відповіді (1–4): "))
        if 1 <= choice <= 4:
            if choice == correct2:
                print("Правильно!")
            else:
                print("Неправильно.")
            break
        else:
            print("Недопустиме значення. Спробуйте ще раз.")
    except ValueError:
        print("Введіть число від 1 до 4.")