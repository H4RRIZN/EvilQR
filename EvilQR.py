#!/usr/bin/python3
import qrcode

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
img.save('eQRCode.png')