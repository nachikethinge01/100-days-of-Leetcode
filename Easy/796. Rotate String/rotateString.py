def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    if ((len(s)) == 0) or ((len(goal)) == 0):
        return True
    possible_list = []
    temp = s
    for i in range(0, len(s)):
        temp = temp[1:] + temp[0]
        possible_list.append(temp)
    return goal in possible_list

print(rotateString("abcde", "cdeab")) #Prints: True --> Expected: True
print(rotateString("abcde", "abced")) #Prints: False --> Expected: False

