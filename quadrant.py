x=int(input("Enter the value of x:"))
y=int(input("Enterbthe value of y:"))

if x>0 and y>0:
    print("First quadrant")
elif x<0 and y>0:
    print("Second quadrant")
elif x<0 and y<0:
    print("Third quadrant")
elif x>0 and y<0:
    print("Fourth quadrant")
elif x==0 and y>0:
    print("Lines at positive y axis")
elif x==0 and y<0:
    print("Lines at negetive y axis")
elif y==0 and x<0:
    print("Lines at negetive x axis")
elif y==0 and x>0:
    print("Lines at positive x axis")
else:
    print("Origin")