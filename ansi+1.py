def chkstr(str):
    result=""
    for i in range(len(str)):
        result=result+str[:i+1]
    return result

a=input("Enter the string:")
if a=="":
    print("Please enter the string")
    exit()
else:
    ans=chkstr(a)
    print("answe is:", ans)
