def findMedianSortedArrays(nums1, nums2) -> float:
    
    nums_merged = nums1 + nums2
    nums_merged.sort()
    
    if len(nums_merged) % 2 == 1:
        return nums_merged[len(nums_merged)//2]
    else:
        return (nums_merged[len(nums_merged)//2-1] + nums_merged[len(nums_merged)//2])/2

print(findMedianSortedArrays([1, 3], [2])) #Prints: 2 -> Expected 2
print(findMedianSortedArrays([1, 2], [3,4])) #Prints: 2.5 -> Expected 2.5