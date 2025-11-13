arr = [5, 2, 6, 9, 0, 1, 8, 6, 0, 8, 2, 7, 1, 9, 0, 8]
def freq(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
print(freq(arr))
