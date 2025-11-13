arr = [1, 2, 3, 4, -1, 77, 29]

def count_in_range(lst, lower, upper):
    return sum(lower <= x <= upper for x in lst)

range_start = 3
range_end = 40

result = count_in_range(arr, range_start, range_end)
print(f"Кількість елементів у діапазоні [{range_start}, {range_end}]: {result}")