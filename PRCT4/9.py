d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 300, 'd':400}

for key, value in d2.items():
    if key in d1:
        d1[key] += value
    else:
        d1[key] = value
print(d1)
with open("9.txt", "w") as f:
    f.write(str(d1))
with open("9.txt", "r") as f:
    print("З файлу: ", f.read())
