sampleDict = {
 'працівник1': {'Ім\'я': 'Іван', 'зарплата': 7500},
 'працівник2': {'Ім\'я': 'Степан', 'зарплата': 8000},
 'працівник3': {'Ім\'я': 'Богдан', 'зарплата': 6500}
}

for key, value in sampleDict.items():
    if value["Ім'я"] == "Богдан":
        value["зарплата"] = 10000

print("Працівники з зарплатою понад 7000:")
for value in sampleDict.values():
    if value["зарплата"] > 7000:
        print(value["Ім'я"])

sampleDict['працівник4'] = {"Ім'я": "Олег", "зарплата": 9000}

sampleDict = {key: value for key, value in sampleDict.items() if value["зарплата"] >= 8500}

print("\nОновлений словник:")
for key, value in sampleDict.items():
    print(f"{key}: {value}")

with open("12.txt", "w") as f:
    f.write(str(sampleDict))
with open("12.txt", "r") as f:
    print("З файлу: ", f.read())