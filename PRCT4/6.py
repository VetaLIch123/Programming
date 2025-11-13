set1 = {10, 20, 30}
set2 = {20, 40, 50}
set3 = set1.difference(set2)
with open("6.txt", "w") as f:
    f.write(str(set3))
with open("6.txt", "r") as f:
    print(f.read())