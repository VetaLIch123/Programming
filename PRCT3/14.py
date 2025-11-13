arr = []
while len(arr) < 10:
    user_input = input("Введіть число: ")
    try:
        number = int(user_input)
        if number not in arr:
            arr.append(number)
    except ValueError:
        print("Будь ласка, введіть дійсне число.")

print("Список досяг 10 елементів:", arr)