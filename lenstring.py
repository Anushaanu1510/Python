a=int(input("Enter the number:"))
str=input("Enter the string:")

if a>len(str):
    print("The entered number is greater than string number")
    exit()
else:
    front=str[:a]
    back=str[a+1:]
    print(front+back)