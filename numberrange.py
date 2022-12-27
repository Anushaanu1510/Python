def check(n):
    if n in range(100,200):
        return True
    else:
        return False

n=int(input("Enter the number:"))
ans=check(n)
print(ans)

#method 2
def check(x):
    if n in range(100,200):
        return True
    else:
        return False

n=int(input("Enter the number:"))
ans=check(n)
print(ans)

#method 3
def check(n):
    if n in range(100,200):
        print("True")
    else:
        print("False")

n=int(input("Enter the number:"))
check(n)