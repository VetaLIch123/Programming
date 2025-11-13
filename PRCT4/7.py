gradeCounts = {"A": 88, "B": 81, "C": 71, "D": 60, "E": 50}
#A
gradeCounts.keys()
print("Всі ключі: ", gradeCounts.keys())
#B
a = gradeCounts.values()
print("Всі значення: ", gradeCounts.values())
#C
gradeCounts.items()
print("Всі пари ключ-значення: ", gradeCounts.items())
#E
total_sum = sum(gradeCounts.values())
count = len(gradeCounts)
average = total_sum / count
print("Середнє значення: ", average)

for values in gradeCounts.values():
    if values > 70:
        print("Всі ключі зі значенням > 70: ", values)

with open("7.txt", "w") as f:
    f.write(str(gradeCounts.keys()))
    f.write("\n")
    f.write(str(gradeCounts.values()))
    f.write("\n")
    f.write(str(gradeCounts.items()))
    f.write("\n")
    f.write(str(average))
    f.write("\n")
    f.write(str(values))
with open("7.txt", "r") as f:
    print("З файлу: ", f.read())