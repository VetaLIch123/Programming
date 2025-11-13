surname = "родич"
name = "віталій"
fathername = "андрійович"

set1 = set(surname)
set2 = set(name)
set3 = set(fathername)

alphabet = set("абвгґдеєжзийіїклмнопрстуфхцчшщьюя")
a = set2 & set3
b = set1 | set2
c = set2 - set1
d = set1.issubset(set3)
e = set1 ^ set2
f = (set1 ^ set2 ^ set3) - ((set1 & set2) | (set2 & set3) | (set1 & set3))
g = alphabet - (set1 | set2 | set3)
print("a) set2 ∩ set3 =", a)
print("b) set1 ∪ set2 =", b)
print("c) set2 - set1 =", c)
print("d) set1 ⊆ set3 =", d)
print("e) set1 Δ set2 =", e)
print("f) Літери лише в одній множині =", f)
print("g) Відсутні в ПІБ літери =", g)
