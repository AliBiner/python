import string
a="Yazilim Bilimi"
print(a)
print(a[0],a[5],a[-1],a[-2])
print(a[2:10])
print(a[:10])
print(a[2:])
print(len(a))


for x in "banana":      #Looping Through a String
    print(x)

txt="Merhaba Yazilim Bilimine Hos Geldiniz"
print("Hos" in txt)

if "hos" in txt:                                        #içindeyse
    print("Evet, 'Hos' bu cumle icinde")

print("ali" not in txt)

if "ali" not in txt:                                    #içinde değilse
    print("Hayır, 'ali' bu cümle icinde degil")

print(txt.upper())          #harfleri büyütme
print(txt.lower())          #harfelri küçültme

txt="    merhaba,   a"
print(txt.strip())              #Metni sola dayar
print(txt.replace("m","j"))     #harfelrin yerini değiştirir. 2 parametre ile çalışır.

print(txt.split(","))           #metni berlittiğin ibarelerin olduğu konumdan ayırır.
print(txt.split("a"))

a="hello"
b="world"
c=a+" "+b
print(c)

"""age=25
txt="My name is Ali, I am" + age
print(txt)                              #string ve integer birleştirilemez.
"""
age1=25
txt="My name is Ali, I am {0}"
print(txt.format(age1))

quantity=3
itemno=100
price=500
myorder="I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))

myorder="I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))


txt="merhaba \"dünya\" hosgeldiniz." #escape characters

"""
\*  single Quote
\\ Backslash
\n new line
\r Carriage Return(satır başı)
\t tab
\b backspace
\f form feed()
\ooo octal value
\xhh hex value
"""







