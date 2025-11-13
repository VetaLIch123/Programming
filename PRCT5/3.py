def average(*nums):
    return sum(nums) / len(nums) if nums else 0

print(average(2, 4, 6, 8))
