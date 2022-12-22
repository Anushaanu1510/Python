def isPalindrome(s):
    return s == s[::-1]

s = input("Enter the string:")
ans = isPalindrome(s)

if ans:
    print("Yes, it is a palindrome")
else:
    print("No, its not a palindrome")
