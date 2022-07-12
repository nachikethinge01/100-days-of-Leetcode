def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.sort(key=bool, reverse=True)


nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(nums1) #Prints[1, 3, 12, 0, 0] -> Expected [1, 3, 12, 0, 0]


nums2 = [0]
moveZeroes(nums2)
print(nums2) #Print(moveZeroes[0]) #Prints: [0] -> Expected: [0]