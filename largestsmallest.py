n = int(input("Enter n:"))
a = []
largest = 1
smallest = 1

for i in range(n):
    a.append(int(input()))

for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
    elif a[i] < smallest:
        smallest = a[i]

print("Largest number is:", largest)
print("Smallest number is:", smallest)
