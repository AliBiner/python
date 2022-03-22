print("ahmet'in bugun dersi var")
print("yazilim")
print("yazilim","bilimi")
print("yazilim"+"bilimi")
print("python",3)
print("yazilim",3,3.4,"bilimi")
print("yazilim",str(3))
print(float('8.5'),5)

"""
Alabileceği parametreler
1-object(s)
2-sep='separator'           *verielen parametreler arasındaki boşluğun şeklini belirler
3-end='end'                 *verilen parametre(ler)in sonuna gelecek sembolü belirtir.
4-file                      *dosyanın içindekileri ekrana yazmaya yarar.
5-flush                     *verilen parametrelerin çıktısı alındığını veya belleğe alındığını True veya False ile gösterir.

"""

print("yazilim","bilimi", sep='---')
print("yazilim",end='@\n')
print("yazilim","bilimi",end='@\n')
print("yazilim","bilimi","merhaba",sep='---',end='@\n')