import secrets

print("Родич Віталій Андрійович, КБ-105, 2025. Варіант 20")

upp = int(input("Введіть кількість великих літер в паролі: "))
low = int(input("Введіть кількість малих літер в паролі: "))
num = int(input("Введіть кількість цифр в паролі: "))
spec = int(input("Введіть кількість спеціальних символів в паролі: "))
upp_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
specials = '!@#$%^&*()-_=+[]{};:,.<>?/|\\'

def pick(chars, count):
    return '' if count == 0 else secrets.choice(chars) + pick(chars, count - 1)

password = (
    pick(upp_letters, upp) +
    pick(low_letters, low) +
    pick(digits, num) +
    pick(specials, spec)
)

def shuffle(text):
    return '' if text == '' else (
        lambda i: text[i] + shuffle(text[:i] + text[i+1:])
    )(secrets.randbelow(len(text)))

password = shuffle(password)

print(f"Пароль: {password}")
