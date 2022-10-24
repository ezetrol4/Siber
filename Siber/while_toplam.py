veri = "Python 101"
egitim = list(veri)
print(egitim)
harf_sayaci = 0
rakam_sayaci = 0
for i in egitim:
    if str(i).isdecimal():
        rakam_sayaci += 1
    else:
        harf_sayaci += 1
print("Rakam sayisi" , rakam_sayaci)
print("Harf sayaci", harf_sayaci)  