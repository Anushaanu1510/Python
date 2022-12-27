def check(n1, n2):
    if n1 == 10 or n2 == 10:
        return True
    elif n1+n2 == 10:
        return True
    else:
        return False


a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
ans=check(a,b)
print(ans)
