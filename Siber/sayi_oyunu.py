import random 
random_sayi = round(random.random()*100)
print(random_sayi)
girilen_sayi = int(input("0 ile 100 arasinda deger giriniz : "))
while random_sayi != girilen_sayi :
    if girilen_sayi > random_sayi :
        print("Girilen deger istenilen degerden buyuktur.")
    else :
        print("Girilen deger istenilen degerden kucuktur.")
    girilen_sayi = int(input("0 ile 100 arasinda deger giriniz : "))
print("Dogru degeri buldunuz !")