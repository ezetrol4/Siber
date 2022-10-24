from cgitb import text
from distutils.cmd import Command
import tkinter
import datetime


def kontrol_et():
    dosya = open("usom.txt" ,"r")
    icerik = dosya.read()
    dosya.close()
    ip = entry1.get()
    bugun = datetime.datetime.now()
    if str(ip) in icerik:
        dosya = open("log.txt" , "a")
        yazi = str(ip) + "zararlı \n Tarih: " +str(bugun) + "\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararlıdır.")
    else:
        dosya.open("log.txt" , "a")
        yazi = str(ip) + "zararlı degildir \n Tarih" + str(bugun) + "\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararlı degildir. ")

top = tkinter.Tk()
top.title("Usom IP Kontrol")
B = tkinter.Button(top, text = "Kontrol Et", command = kontrol_et)
B.place(x = 50 ,y = 50)
B.pack()
label1 = tkinter.Label(top, text="Kontrol edilecek IP adresini giriniz.")
label1.place(x=50 , y=80)
label1.pack()
entry1 = tkinter.Entry(top)
entry1.place(x=50 , y=90)
entry1.pack()
v = tkinter.StringVar()
entry2 = tkinter.Entry(top , textvariable=v)
entry2.place(x=50 , y=100)
entry2.pack()
top.mainloop()