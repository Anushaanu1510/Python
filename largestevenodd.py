n=int(input("Enter n numbers"))
n_array=[]

for i in range(0,n):
    n_array.append(int(input()))

even_max=-1
odd_max=-1

for i in range(0, n):
    if(n_array[i]%2==0 and n_array[i]>even_max):
        even_max=n_array[i]

    elif(n_array[i]%2!=0 and n_array[i]>odd_max):
        odd_max=n_array[i]

print("Largest even number:", even_max)
print("Largest odd number:", odd_max)

    
