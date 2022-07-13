def uncommonFromSentences(s1: str, s2: str):
    
    lst1 = [word for word in s1.split()] + [word for word in s2.split()]
    temp = set([i for i in lst1 if lst1.count(i) == 1])
    return (list(temp))

print(uncommonFromSentences("this apple is sweet", "this apple is sour")) #Prints: [Sour Sweet] -> Expected: [Sour, Sweet]
print(uncommonFromSentences("apple apple", "banana")) #Prints: [Banana] -> Expected: [Banana]