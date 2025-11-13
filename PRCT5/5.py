def count_letters(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

print(count_letters('Слава Україні'))  # (2, 10)
