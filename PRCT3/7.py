def find_long_words(word_list, n):
    long_words = []
    for word in word_list:
        if len(word) > n:
            long_words.append(word)
    return long_words

list_of_words = ['abc', 'xyz', 'aaaa', 'aba', '1221']
n_value = 3
result = find_long_words(list_of_words, n_value)
print(result)