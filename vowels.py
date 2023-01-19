string = input("Enter the string")
v=0
c=0

for i in string:
    if i in ['a','e','i','o','u']:
        v=v+1
    else:
        c=c+1
print("This string contains",v,"vowels")
print("This string contains",c,"consonents")