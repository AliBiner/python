"""
yas= int(input("yasınızı giriniz:"))

if yas>=18:
    print("Yası 18 den buyuktur.")

else :
    print("yası 18 den kucuktur.")


note=float(input("Puanı giriniz:"))

if note>=90:
    print("AA")
elif note>=85:
    print("BA")
elif note>=80:
    print("BB")
else:
    print("Dersten kaldınız.")


defuser="ali"
defpassword="1234"

user=input("Kullanici adi giriniz:")
password=input("sifre giriniz:")

if user==defuser and password==defpassword:
    print("giris basarili")

elif user!=defuser and password==defpassword:
    print("Kullanici adi yanlis")

elif password!=defpassword and user==defuser:
    print("parola yanlis")

else:
    print("Kullanici adi ve parola yanlis")
"""
a=33
b=200
if b>a:
    pass

