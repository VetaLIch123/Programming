d1 = {'a': 100, 'b': 200, 'c': 300}
value_to_find = 200
if value_to_find in d1.values():
    print("Потрібне значення: ", value_to_find)
with open("10.txt", "w") as f:
    f.write(str(value_to_find))
with open("10.txt", "r") as f:
    print("З файлу: ", f.read())
