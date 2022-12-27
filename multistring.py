import time


def multistring(a, b):
    result = ""
    for i in range(a):
        result = result+b
    return result


a = int(input("Enter the value od a:"))
b = input("Enter the string:")
if a < 0:
    print("Enter a positive number")
    time.sleep(5)
    exit()
else:
    ans = multistring(a, b)
    print(ans)
