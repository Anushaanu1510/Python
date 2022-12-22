list1=[11,22,33,44,55,66,77,88,99,101]


even_max=0
odd_max=0

for i in range(len(list1)):
    if(list1[i]%2==0):
        if (list1[i]>even_max):
            even_max=list1[i]
    elif(list1[i]%2!=0):
        if (list1[i]>odd_max):
            odd_max=list1[i]
        

print("Largest even number is",even_max)
print("Largest odd number is",odd_max)      
