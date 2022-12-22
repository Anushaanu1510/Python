n=int(input("Enter the number"))

fact=1

if n<0:
    print("Enter thge positive number")
elif n==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, n+1):
        fact=fact*i
    print("Factorial of ", n ,"is", fact) 
