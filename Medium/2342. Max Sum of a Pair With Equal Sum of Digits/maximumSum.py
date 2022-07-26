from collections import defaultdict


def maximumSum(nums) -> int:
    
    res = -1
    table = defaultdict(list)
    
    for num in nums:
        table[sum(int(digit) for digit in str(num))].append(num)

    for num, val in table.items():
        if len(val) <= 1: 
            continue
        val.sort()
        res = max(res, sum(val[-2:]))
        
    return res

print(maximumSum([18,43,36,13,7])) #Prints: 54 -> Expected: 54
print(maximumSum([10,12,19,14])) #Prints: -1 -> Expected: -1