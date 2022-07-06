def intToRoman(num: int) -> str:
    data = {
        1 : "I",
        4 : "IV",
        5 : "V",
        9 : "IX",
        10 : "X",
        40 : "XL",
        50 : "L",
        90 : "XC",
        100 : "C",
        400 : "CD",
        500 : "D",
        900 : "CM",
        1000 : "M"
    }
    
    n = num
    romanStr = ""
    
    while n > 0:
        if n >= 1000:
            romanStr += data[1000]
            n -= 1000
            
        elif n >= 900:
            romanStr += data[900]
            n -= 900
            
        elif n >= 500:
            romanStr += data[500]
            n -= 500
            
        elif n >= 400:
            romanStr += data[400]
            n -= 400
            
        elif n >= 100:
            romanStr += data[100]
            n -= 100
            
        elif n >= 90:
            romanStr += data[90]
            n -= 90
            
        elif n >= 50:
            romanStr += data[50]
            n -= 50
            
        elif n >= 40:
            romanStr += data[40]
            n -= 40
            
        elif n >= 10:
            romanStr += data[10]
            n -= 10
            
        elif n >= 9:
            romanStr += data[9]
            n -= 9
        
        elif n >= 5:
            romanStr += data[5]
            n -= 5
            
        elif n >= 4:
            romanStr += data[4]
            n -= 4
        
        elif n >= 1:
            romanStr += data[1]
            n -= 1
        
    return romanStr

print(intToRoman(3)) #Prints: III -> Expected: III
print(intToRoman(58)) #Prints: LVIII -> Expected: LVIII
print(intToRoman(1994)) #Prints: MCMXCIV -> Expected: MCMXCIV