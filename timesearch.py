def chkstr(str):
    result=""
    for i in range(len(str)):
        result=result+str[:i+1]
    return result

def timesearch(a,k):
    result1=a.count(k)
    return result1

a=input("Enter the string:")
key=input("Enter the search string:")
if a=="":
    print("Please enter the string")
    exit()
else:
    ans=chkstr(a)
    answer1=timesearch(ans,key)
    print("the number of times", key, "found in", ans, "is:", answer1)