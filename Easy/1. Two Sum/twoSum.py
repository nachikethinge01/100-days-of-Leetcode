def twoSum(nums, target: int):    
    for i, n in enumerate(nums):
        if target - n in nums and i != nums.index(target - n):
            return sorted([i, nums.index(target-n)])

print(twoSum([2, 7, 11, 15], target=9)) #Prints: [0, 1] -> Expected: [0, 1]
print(twoSum([3, 3], target = 6)) #Prints: [0, 1] -> Expected: [0, 1]




