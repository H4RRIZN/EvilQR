#!/usr/bin/python3
import qrcode
from alive_progress import alive_bar
from time import sleep
from os import system


URL = input("Ingresa una URL: ")

# QR 
qr = qrcode.QRCode(
    version=4,
    box_size=10,
    border=1
)

qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

print("Generando Codigo QR\n")

# QR GENERATING
with alive_bar(100, spinner='pulse') as progrs:
    for i in range(100):
        sleep(0.01)
        progrs()
print("\nQR Generado con exito [!]")
print("Archivo almacenado en la carpeta del repositorio: EvilQR/eQRCode.png ")
sleep(3)
system('clear')
img.save('eQRCode.png')