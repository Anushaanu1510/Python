print("Python program to check whether storing begins with not")
str=input("Enter a string:")

if str.startswith("Not") or str.startswith("not"):
    print(str,"This string starts with 'Not', no improvements needed")
else:
    print("Not", str,"This string does not starts with 'Not', so added 'Not'")