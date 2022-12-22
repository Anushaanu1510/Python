
n=0
num=0
max=0

    
while n<10:
    num=int(input("Enter n numbers"))
    if num % 2==0:
        if num>max:
            max=num
    n+=1
print("Maximum even number is :",max)

