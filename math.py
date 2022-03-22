import math
math.ceil(32.05) #verilen ondalıklı sayıyı üst sayıya çevirir.
math.floor(25.98) #verilen ondalıklı sayıyı aşağı sayıya yuvarlar.
math.copysign(25,-15) #verilen ikinci sayının işareti ilk sayıya geçer.
math.fabs(-28) #mutlak değeri alınır. "abs"den farkı ondalıklı sonuç vermesidir.
math.factorial(5) #faktoriyeli alınır. (-) lerde çalışmaz.
math.fmod(45,2) #birinci parametrenin ikinci parametreye bölümünden kalanı bulunur.
math.frexp() # m * 2 ** e işlemininde m ve e yi bulmaya yarar.
math.fsum([]) #içindeki değerlerin toplamını verir.
math.gcd(45,70) # ebobunu bulmayı sağlar.
math.e  # euler sabitini tutan değişken. değeri:2.718281...
math.pi # pi sayısını tutan değişken
math.tau #tau sabitini tutan değişken. değeri pi sayısının 2 katıdır.
math.exp() #euler sabitinin kuvvetini alır.
math.expm1() #math.exp nin sonucundan 1 çıkmış halidir
math.log() #logaritma alır
math.log1p() #verilen sayının bir fazlasının e tabanına göre logaritmasını alır
math.log2()  #2 tabanına göre log
math.log10() #10 tabanına göre log
math.pow() #birinci sayının ikinci sayıya göre kuvveti alınır
math.sqrt() # karekök alma
math.degrees() #radyandan dereceye çevirme
math.radians() # dereceden radyana çevirme
math.sin(math.radians(60)) # radyan cinsinden sayıyı sinüsü hesağlama
math.cos()
math.tan()
math.asin() #verilen sinüs değerinde radyan cinsinde bir açı döndürür
math.acos()
math.atan()
math.atan2(45,90) # atan(90/45) sonucunu dönderir
math.hypot() # sqrt(x*x+y*y) sonucu döner
math.sinh() #hiperbolik sinüsü döner
math.cosh()
math.tanh()
math.asinh() # tersine dönderir
math.acosh()
math.atanh()
math.gamma() #faktoriyel fonksiyonuna çok benziyor. verilen sayının 1 azının faktoriyeli hesaplanıyor. ancak asıl fark sayı büyüdüğünde ortaya çıkıyor.
math.factorial(12) == math.gamma(13)
"""math.factorial(12) =>  479001600
math.gamma(13) => 479001600.0
math.factorial(35) => 10333147966386144929666651337523200000000
math.gamma(36) => 1.0333147966386145e+40"""
math.lgamma() # gamma nın logaritmasını alır.





