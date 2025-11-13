ukr_letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
a, b = 14, 21
n = len(ukr_letters)

def mod_inverse(a, n):
    for i in range(1, n):
        if (a * i) % n == 1:
            return i
    raise ValueError("Оберненого елемента не існує")

a_inv = mod_inverse(a, n)

ciphertext = "и узпсбек, юз кщ, вґсяяє, пзлстїпзьз ґзхй"

plaintext = ''
for c in ciphertext:
    if c not in ukr_letters:
        plaintext += c
    else:
        y = ukr_letters.index(c)
        dec_x = (a_inv * (y - b)) % n
        plaintext += ukr_letters[dec_x]

print("Розшифрований текст:", plaintext)