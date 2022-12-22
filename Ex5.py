#x = int(input("Enter the value for x"))
#y = int(input("Enter the value for y"))
#z = x + y
#print(z)

a = "hello how are you"
print(a)

greet = [1,100,"hi", "welcome", "hola", "hi", "bonjour", "salve", "welcome", "hello", "howdy", "hola"]
print(greet)
greet = ["hi", "welcome", "hola", "hi", "bonjour", "salve", "welcome", "hello", "howdy", "hola"]
print(set(greet))
#duplicates are not allowed
print(greet.count("hi"))
greet = ["hi", "welcome", "hola", "hi", "bonjour", "salve", "welcome", "hello", "howdy", "hola"]
counts=[]
for i in greet:
    if i in counts:
        counts[i]+=1
    else:
        counts[i]= 1

print(counts.get('hi'))
