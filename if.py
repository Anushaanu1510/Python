#if statement
x=int(input("Enter the number"))
if x<0:
    x=0
    print(x)
    print("Negetive converted into zero")
elif x==0:
    print("Zero")
elif x==1:
    print("Single")
else:
    print("More")

