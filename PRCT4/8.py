dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
with open("8.txt", "w") as f:
    f.write(str(dic1))
with open("8.txt", "r") as f:
    print("З файлу: ", f.read())