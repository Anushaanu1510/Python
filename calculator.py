a = int(input("Enter the value of a:"))
b = int(input("Enter the value for b:"))


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


print("The sum of", a, "and", b, "is", add(a, b))
print("The difference of", a, "and", b, "is", subtract(a, b))
print("The product of", a, "and", b, "is:", multiply(a, b))
print("The division of", a, "and", b, "is:", divide(a, b))
