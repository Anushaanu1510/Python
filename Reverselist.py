thislist1=["apple","banana","cherry"]
thislist1.extend(["mango","blackcurrent"])
print(thislist1)

thislist2=thislist1[::-1]
print(thislist2)

#using for loop
thislist1=["apple","banana","cherry","mango","blackcurrent"]
thislist2=[]

for items in thislist1:
    thislist2=[items]+thislist2
print(thislist2)

thislist1=["apple","banana","cherry","mango","blackcurrent"]
thislist1[0]="blackcurrent"
thislist1[1]="mango"
thislist1[2]="cherry"
thislist1[3]="banana"
thislist1[4]="apple"
print(thislist1)
