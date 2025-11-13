list1 = [1, 2, 2, 3, 4, 4, 5, 1, 6 ,2, 8, 0, 3, 5, 6, 7]
list2 = [5, 2, 6, 9, 0, 1, 8, 6, 0, 8, 2, 7, 1, 9, 0, 8]

set1 = set(list1)
set2 = set(list2)
diff = set1.difference(set2)
result = list(diff)
print(result)