lst = ["Java", "Algol", "Python"]
result = max(lst, key=lambda x: x.lower().count('a'))
print(result)
