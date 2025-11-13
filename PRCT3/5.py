arr =  ['abc', 'xyz', 'aba', '1221', '1232']
def filter_long_words(word_list, n):
    return [word for word in word_list if len(word) > n]

n = 3
result = filter_long_words(arr, n)
print(result)
