def reverse(x: int) -> int:
    
    st = str(abs(int(x)))
    reverse = int(st[::-1])
    
    if reverse < -(2**31) or reverse > (2**31) - 1:
        return 0
    
    if x < 0:
        return reverse * -1
    return reverse

print(reverse(123)) #Prints: 321 -> Expected: 321
print(reverse(120)) #Prints: 21 -> Exptected 21
print(reverse(-123)) #Prints: -321 -> Exptected: -321