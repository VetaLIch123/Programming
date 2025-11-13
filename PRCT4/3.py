tpl = ('в', 5, 'п', 'р', 'а', 'в', 'a')
new_list = []
for item in tpl:
    if not isinstance(item, int):
        new_list.append(item)
open('3.txt', 'w').writelines(new_list)
with open('3.txt', 'r') as f:
    print(f.read())