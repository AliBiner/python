mylist=["apple","banana","cherry"]
print(mylist)
print(len(mylist))

list1=["apple","banana","cherry"]
list2=[1,5,7,9,3]
list3=[True,False,False]
print(list1)
print(list2)
print(list3)

list1=["apple",3,3.7,True]

print(type(list1))

thislist=list1

print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[1:])
print(thislist[-4:-1])

if "apple" in thislist:
    print("yes")

thislist[1]="blackmamba"
print(thislist)

thislist[1:3]=["blackmamba","lemon"]
print(thislist)

thislist[3:4]=["merhaba","ali"]
print(thislist)

thislist[1:3]=["saturn"]
print(thislist)

thislist.insert(2,"watermelon")
print(thislist)

thislist.append("orange")
print(thislist)

thislist.insert(1,"orange")
print(thislist)

tropical=["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)

thistuple=("kiwi","orange")
thislist.extend(thistuple)
print(thislist)

thislist.remove("apple")
print(thislist)

thislist.pop(1)
print(thislist)

thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

"""del thislist
print(thislist)"""

thislist.clear()
print(thislist)

thislist=["apple","banana","cherry"]

for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1

[print(x) for x in thislist]

newlist = []

for x in thislist:
    if "a" in x:
        newlist.append(x)

print(newlist)

thislist=["apple","cherry","banana"]
thislist.sort()
print(thislist)

thislist=["apple","cherry","banana"]
thislist.sort(reverse=True)
print(thislist)

mylist=thislist.copy()
print(mylist)

mylist=list(thislist)
print(mylist)

list4=list3+list2
print(list4)




