elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be"), (11, 79, "Au")]
elements.sort(key=lambda x: x[1])
print(elements)
