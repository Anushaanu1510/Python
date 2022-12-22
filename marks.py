name=input("Enter the name of the student:")
age=int(input("Enter the age:"))
pno=input("Enter the phone number:")
m1=int(input("Enter the marks in subject 1:"))
m2=int(input("Enter the marks in subject 2:"))
m3=int(input("Enter the marks in subject 3:"))
m4=int(input("Enter the marks in subject 4:"))
m5=int(input("Enter the marks in subject 5:"))

def calculate():
    if m1>10 and m2>10 and m3>10 and m4>10 and m5>10:
        total_marks=m1+m2+m3+m4+m5
        avg=total_marks/5
        print("Name:",name)
        print("Age:",age)
        print("Phone number:",pno)
        print("Marks in subject 1:",m1)
        print("Marks in subject 2:",m2)
        print("Marks in subject 3:",m3)
        print("Marks in subject 4:",m4)
        print("Marks in subject 5:",m5)
        print("Total marks is:",total_marks)
        print("Average is",avg)
    else:
        print("Marks in each subject should be greater than 1o")

calculate()
