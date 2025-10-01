ukr_upp_char = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
ukr_low_char = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

def caesar_encrypt(text, k):
    result = ""
    for ch in text:
        if ch in ukr_upp_char:
            i = (ukr_upp_char.index(ch) + k) % len(ukr_upp_char)
            result += ukr_upp_char[i]
        elif ch in ukr_low_char:
            i = (ukr_low_char.index(ch) + k) % len(ukr_low_char)
            result += ukr_low_char[i]
        else:
            result += ch
    return result

def caesar_decrypt(text, k):
    return caesar_encrypt(text, -k)

msg = input("Введіть текст:")
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)

print("Відкритий текст:", msg)
print("Зашифрований:", enc)
print("Розшифрований:", dec)
