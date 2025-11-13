tpl = ('в', 'п', 'р', 'а', 'в', 'a', 2)
separator = ''
my_tpl = separator.join(map(str, tpl))
with open("2.txt", "w") as f:
    f.write(my_tpl)
with open("2.txt", "r") as f:
    print(f.read())