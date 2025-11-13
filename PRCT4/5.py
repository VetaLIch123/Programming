set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50,}
set3 = set1.intersection(set2)
with open("5.txt", "w") as f:
    f.write(str(set3))
with open("5.txt", "r") as f:
    print(f.read())