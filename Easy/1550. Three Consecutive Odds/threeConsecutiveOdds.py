def threeConsecutiveOdds(arr) -> bool:
    
    count_odd = 0
    
    for i in arr:
        if count_odd == 3:
            break
        elif i % 2 == 1:
            count_odd += 1
        else:
            count_odd = 0
    return count_odd == 3


list1 = [2,6,4,1]
print(threeConsecutiveOdds(list1)) #Prints: False -> Expected: False

list2 = [1,2,34,3,4,5,7,23,12]
print(threeConsecutiveOdds(list2)) #Prints: True -> Expected: True