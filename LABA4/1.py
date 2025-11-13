n = 40858
a = 8173
b = 24478

print("Квадрати чисел менші за n:", [i**2 for i in range(1, int(n**0.5) + 1)])

print("Числа кратні 100 менші за n:", [i for i in range(100, n, 100)])

print("Всі степені двійки менші ніж n:", [2**i for i in range(n.bit_length()) if 2**i < n])

print("Сума парних чисел між a та b:", sum(i for i in range(a, b + 1) if i % 2 == 0))

print("Сума непарних чисел між a та b:", sum(i for i in range(a, b + 1) if i % 2 != 0))

print("Сума непарних цифр числа n:", sum(int(d) for d in str(n) if int(d) % 2 != 0))