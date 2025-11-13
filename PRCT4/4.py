tpl =[('item1', 12.20), ('item2', 15.10), ('item3', 24.5)]
my_list = list(tpl)

my_list.sort(reverse=True)
sorted_tuple = tuple(my_list)
with open("4.txt", "w") as f:
    f.write(str(my_list))
with open("4.txt", "r") as f:
    print(f.read())