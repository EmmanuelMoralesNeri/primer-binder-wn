#print("Hola, qué hace? ")

# Velocidad de internet
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
from speedtest import Speedtest

def test_velocidad():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    ping_lbl.config(text=str(speed_test.result.ping))
    download_speed = round(download/(10**6), 2)
    upload_speed = round(upload/(10**6), 2)
    down_lbl.config(text=str(download_speed))
    up_lbl.config(text=str(upload_speed))
    
    
ventana = Tk()
ventana.title("Internet Speed Tracker")
ventana.config(bg="#292629")
ventana.iconbitmap("Masked.ico")
ventana.resizeable(False, False)


# Cargar imagen
img = PhotoImage(file="t")
img_lbl = Label(ventana, imagen=img, bg="#292629")
img_lbl.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# 
imagen2 = Image.open(".png")
imagen2 = imagen2.resize((400,50), Image.ANTIALIAS)
imagen2 = ImageTk.PhotoImage(imagen2)
img_lbl2 = Label(ventana, image=imagen2, bg="#292629")
img_lbl2.grid(row=1, column=0, columnspan=3, padx=5)

ping_lbl = Label(ventana, text="---", bg="#292629", 
                 font=("AR CHRISTY", 15), fg="white", anchor=CENTER)
ping_lbl.grid(row=2, column=0, padx=5)
down_lbl = Label(ventana, text="---", bg="#292629", 
                 font=("AR CHRISTY", 15), fg="white", anchor=CENTER)
down_lbl.grid(row=2, column=1, padx=5)
up_lbl = Label(ventana, text="---", bg="#292629", 
               font=("AR CHRISTY", 15), fg="white", anchor=CENTER)
up_lbl.grid(row=2, column=2, padx=5)

btn = Button(ventana, text="Get Speed", command=test_velocidad, width=15, bg="#81b1d7")
btn.grid(row=3, column=0, columnspan=3, pady=5)

ventana.mainloop()
