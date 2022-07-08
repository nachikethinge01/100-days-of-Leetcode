def maximumSwap(num: int) -> int:
        
    maxn = sorted(list(str(num)))[::-1]
    toList = list(str(num))
    large_pos = 0
    
    for i in range(len(toList)):
        if toList[i] != maxn[i]:
            for j in range(len(toList)-1, -1, -1):
                if toList[j] == maxn[i]:
                    large_pos = j
                    break
            toList[large_pos], toList[i] = toList[i], maxn[i]
            break
    return int(''.join(str(x) for x in toList))

print(maximumSwap(2736)) #Prints: 7236 -> Expected: 7236
print(maximumSwap(9973)) #Prints 9973 -> Expected: 9973

