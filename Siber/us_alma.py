us = int(input("Us :"))
taban = int(input("Taban :"))
sonuc = 1
for i in range(1,us+1,1):
    sonuc *= taban
print(sonuc)