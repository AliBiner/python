import time

print("Oyuncu Kayıt Programı")
name=input("Oyuncunun adını giriniz:")
surname=input("oyuncunun soyadını giriniz:")
team=input("oyuncunun takımını giriniz:")

informatins=[name,surname,team]

print("Oyuncu Bilgileri Kaydediliyor...")

time.sleep(2)

print("Kaydedildi.")

time.sleep(2)

print( "Oyuncu Adı:" , informatins[0] , "\nOyuncunun soyadı:" , informatins[1] , "\nOyuncunun takımı:" , informatins[2] )

#deneme2