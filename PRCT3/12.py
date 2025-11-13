arr = [5, 2, 6, 9, 0, 1, 8, 6, 0, 8, 2, 7, 1, 9, 0, 8]
def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

sort(arr)
print(arr)