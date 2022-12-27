def absolute(x):
    if x < 21:
        ans = n-21
        print(x, "is less than 21")
        return ans
    else:
        ans = n-21
        ans1 = ans*ans
        print(x, "is greater than 21")
        print("Doubled value is", ans1)
        return ans


print("Printing the absolute value of n")
n = int(input("Enter the value of n:"))
ans1 = absolute(n)
print("The difference between",n,"and 21 is",abs(ans1))

