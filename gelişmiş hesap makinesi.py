import math
import time
from fractions import Fraction
print(""""

******************************
Gelişmiş Hesap Makinesi
******************************
1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
5.Karekök alma
6.Üs alma
7.Faktöriyel
8.Sinüs
9.Kosinüs
10.Tanjant
11.Logaritma
12.Çıkış
******************************
""")

while True:
    giris = int(input("Yapmak istediğiniz işlemi giriniz:"))
    if (giris == 1):
        a = int(input("İşlem yapmak istediğiniz ilk sayıyı giriniz:"))
        b = int(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz:"))
        print("{} + {} = {}".format(a,b,a+b))
    elif giris == 2 :
        a = int(input("İşlem yapmak istediğiniz ilk sayıyı giriniz:"))
        b = int(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz:"))
        print("{} - {} = {}".format(a, b, a - b))
    elif giris == 3 :
        a = int(input("İşlem yapmak istediğiniz ilk sayıyı giriniz:"))
        b = int(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz:"))
        print("{} x {} = {}".format(a, b, a * b))
    elif giris == 4 :
        a = int(input("İşlem yapmak istediğiniz ilk sayıyı giriniz:"))
        b = int(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz:"))
        print("{} / {} = {}".format(a, b, a / b))
    elif giris == 5 :
        a = int(input("Karekökünü almak istediğiniz  sayıyı giriniz:"))
        if a > 0:
            print(math.sqrt(a))

    elif giris == 6 :
        a = int(input("Üssünü almak istediğiniz  sayıyı giriniz:"))
        b = int(input("Kaçıncı üssünü almak istiyorsunuz:"))
        print("{}^{} = {}".format(a, b, a ** b))
    elif giris == 7 :
        a = int(input("Faktöriyelini almak istediğiniz  sayıyı giriniz:"))
        if a <= 0:
            print("Girdiğiniz sayının faktöriyeli alınamaz başka bir sayı giriniz !")
            a = int(input("Faktöriyelini almak istediğiniz  sayıyı giriniz:"))
            print("sonuç =",math.factorial(a))
        else:
            print("sonuç =",math.factorial(a))
    elif giris == 8 :
        a = int(input("Sinüsünü almak istediğiniz sayıyı giriniz:"))
        print("Sonuç =",math.sin(math.radians(a)))
    elif giris == 9 :
        a = int(input("Kosinüs almak istediğiniz sayıyı giriniz:"))
        print("Sonuç =", math.cos(math.radians(a)))
    elif giris == 10 :
        a = int(input("Tanjantını almak istediğiniz sayıyı giriniz:"))
        print("Sonuç =", math.tan(math.radians(a)))
    elif giris == 11 :
        a = int(input("Logaritmasını almak istediğiniz sayıyı giriniz:"))
        if a <= 0 :
            print("Girdiğiniz sayının logaritması alınamaz başka bir sayı giriniz !")
            a = int(input("Logaritmasını almak istediğiniz sayıyı giriniz:"))
            print("sonuç =",math.log10(a))
        else:
            print("sonuç =", math.log10(a))
    elif giris == 12 :
        print("Hesap makinesi kapatılıyor...")
        time.sleep(1)
        print("Hesap makinesi kapatıldı")
        break






