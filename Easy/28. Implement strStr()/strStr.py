def strStr(haystack: str, needle: str) -> int:
    
    if len(needle) == 0 or haystack == needle:
        return 0

    increment = len(needle)
    
    for i in range(0, len(haystack)-increment+1):
        if(haystack[i:i+increment] == needle):
            return i
    
    return -1

haystack1 = "hello"
needle1 = "ll"
print(strStr(haystack1, needle1)) #Prints: 2 -> Expected: 2

haystack2 = "aaaaa"
needle2 = "bba"
print(strStr(haystack2, needle2)) #Prints: -1 -> Expected: -1



        

