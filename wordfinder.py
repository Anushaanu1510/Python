def wordfinder(s1, s2):
    word = list(s1.split(" "))
    count = 0
    for x in word:
        if x == s2:
            count = count+1
    if count == 0:
        print(s2," does not found")
    return count


a = input("Enter the string:")
b = input("Enter the word has to be searched:")
ans=wordfinder(a, b)
print(ans)