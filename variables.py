print(type(12))
print(type(2.34))
print(type("python"))
print(type([1,2,3,4]))
print(type((1,2,3,4)))
print(type({"elma":"meyve"}))

x=5
y=6
x=x+y
print(x)

ilk="yazilim"
son="bilimi"
ilk=ilk+son
print(ilk)

x=34
print(type(x))
print(type(str(3)))
print(float(3))
print(int(3.7))

a=4
A=5

myvar=4
my_var=4
_my_var=4
myVar=4
MYVAR=4
myvar2=4

"""
2myvar=4
my-var=4
my var=4
"""

x,y,z="ali","biner",25
print(x,y,z)

x=y=z="ali"
print(x,y,z)

meyveler="elma","muz","domates"
x,y,z=meyveler
print(x,y,z)

x="ali"

def myfunc():
    x="biner"
    print(x)
myfunc()

print(x)

def myfunc2():
    global x
    x="biner"
myfunc2()
print(x)
