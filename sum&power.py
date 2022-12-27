import math


def getsum(n1, n2):
    n3 = n1+n2
    return n3


def getsumsq(n1, n2):
    n3 = n1+n2
    n4 = math.pow(n3, 2)
    return n4


a = int(input("enter the first number"))
b = int(input("Enter the second value:"))

if a!=b:
    print("Two values are different")
    ans=getsum(a,b)
    print("The sum of", a , "and", b,"is:",ans)
else:
    print("Two values are equal")
    ans=getsumsq(a,b)
    print("The sum of ",a,"+",b ,"is:", a+b,"and the square of the answer is",ans)