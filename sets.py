basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  

if 'orange' in basket:
    print("True")
else:
    print("False")  
if 'crabgrass' in basket:
    print("True")
else:
    print("False")  

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b) 

print(a-b)#unique

print(a|b)#intersection

print(a&b)#both in a and b

print(a^b)#letters in a not in b

print(b^a)#letters in b not in a

