def firstMissingPositive(nums) -> int:
    
    nums.sort()
    temp = 1
    
    for i in nums:
        if i == temp:
            temp += 1
    return temp

print(firstMissingPositive([1, 2, 0])) #Prints: 3 -> Expected: 3
print(firstMissingPositive([3, 2, 4])) #Prints: 1 -> Expected: 1
