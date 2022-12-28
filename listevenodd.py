n = int(input("Enter the number of elements to be added:"))
a = []

even = []
odd = []
count=0
count1=0
evenmax = 0
oddmax = 0

for i in range(n):
    a.append(int(input()))

print(a)

for i in range(len(a)):
    if (a[i] % 2 == 0):
        even.append(a[i])
        count=count+1
        if (a[i] > evenmax):
            evenmax = a[i]
    elif (a[i] % 2 !=0):
        odd.append(a[i])
        count1=count1+1
        if (a[i] > oddmax):
            oddmax = a[i]

print("Even numbers in the list are:", even)
print("Count of even numbers are:",count)
print("Largest even number is:", evenmax)
print("Odd numbers in the list are:", odd)
print("Count of odd numbers are:",count1)
print("Largest odd number is:", oddmax)