def remove_duplicates_loop(input_list):
  unique_list = []
  for item in input_list:
    if item not in unique_list:
      unique_list.append(item)
  return unique_list

arr = [1, 2, 2, 3, 4, 4, 5, 1, 6 ,2, 8, 0, 3, 5, 6, 7]
new_list = remove_duplicates_loop(arr)
print(new_list)