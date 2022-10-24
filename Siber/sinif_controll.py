a_sinif = ["Ahmet","Mehmet"]
b_sinif = ["Ali","Ayşe"]

isim =input("İsim giriniz: ")

if isim in a_sinif:
    print("Kişi a sınıfındadır")
elif isim in b_sinif:
    print("Kişi b sınıfındadır")
else:
    print("Kişi sınıflarda bulunamamıştır")