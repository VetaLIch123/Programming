with open("1.txt", "w") as f:
    f.write(str(tuple(range(0,100))))
a = open("1.txt", "r")
b = a.read()
print(b)