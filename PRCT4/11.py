text = input("Введіть рядок:")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)
with open("11.txt", "w") as f:
    f.write(str(frequency))
with open("11.txt", "r") as f:
    print("З файлу: ", f.read())