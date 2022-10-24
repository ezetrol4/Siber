import string


islem = input("Islemi giriniz:")

sayi1 = int(input("Sayi1: "))

sayi2 = int(input("Sayi2: "))


if islem == "1" :
    sonuc = int(sayi1) + int(sayi2)
    print("Sonuc:" , str(sonuc))
elif islem == "2" :
    sonuc = int(sayi1) * int(sayi2)
    print ("Sonuc:" , str(sonuc))
elif islem == "3":
    sonuc = int(sayi1) - int(sayi2)
    print("Sonuc:", str(sonuc))
elif islem == "4":
    sonuc = int(sayi1) / int(sayi2)
    print("Sonuc:", str(sonuc))