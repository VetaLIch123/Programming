n = 2
step = 3
size = 15
arr = [3*n**2 + 2*n + 1 for n in range(n, n + step*size, step)]
print("Початковий список:", arr)

print("Елементи з індексами 3–5:", arr[3:6])

arr_b = arr.copy()
arr_b[0] = arr_b[-1]
print("Список після заміни першого елемента останнім:", arr_b)

combined = arr + arr_b
print("Об'єднаний список:", combined)

combined += combined[:3]
print("Після додавання перших трьох:", combined)

print("Максимум:", max(combined), "Мінімум:", min(combined))

avg = sum(combined) / len(combined)
filtered = [x for x in combined if x >= avg]
print("Список після видалення елементів менших за середнє:", filtered)
print("Середнє значення:", avg)
