def lengthOfLongestSubstring(s: str) -> int:
    
    if len(s) <= 1:
        return len(s)
    
    
    holder = []
    all_strings = []
    all_strings.append("".join(holder))
    
    for letter in s:
        if letter not in holder:
            holder.append(letter)
        else:
            all_strings.append("".join(holder))
            get_index = holder.index(letter)
            del holder[:get_index+1]
            holder.append(letter)
    
    if len(holder) > 0:
        all_strings.append("".join(holder))
        

    return len(sorted(all_strings, key = len, reverse=True)[0])

print(lengthOfLongestSubstring("abcabcbb")) #Prints: 3 -> Expected: 3
print(lengthOfLongestSubstring("bbbbb")) #Prints: 1 -> Expected: 1
print(lengthOfLongestSubstring("pwwkew")) #Prints: 3 -> Expected: 3