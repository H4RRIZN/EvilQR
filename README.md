# EvilQR
<p align="center">
   <img src="https://github.com/Harrizzon/EvilQR/blob/main/misc/EvilQR-Logo.jpg" width="350" title="RSCS">
<p align="center">
<p align="center">
   <a href="https://github.com/Harrizzon/EvilQR"><img src="http://ForTheBadge.com/images/badges/built-with-love.svg"> <img src="https://forthebadge.com/images/badges/made-with-python.svg"></a>
<p align="center">

EvilQR es una herramienta escrita en python que permite generar códigos QR con alguna URL maliciosa o similar. Esta además permite enmascarar las URL para añadir un nivel de ingeniería social más elevado.

# Features
- Generar Codigo QR en base a cualquier tipo de URL
- Enmascarar URL

# Instalación

One Liner 
```bash
# Install as sudo
sudo su
git clone https://github.com/Harrizzon/EvilQR && cd EvilQR && chmod +x EvilQR.py && pip3 install -r requirements.txt && cp EvilQR.py /usr/bin/
```
By Steps
```bash
# Install as sudo
sudo su
git clone https://github.com/Harrizzon/EvilQR
cd EvilQR
chmod +x EvilQR.py
pip3 install -r requirements.txt

# Optional but recommendable
cp EvilQR.py /usr/bin/
```

# Uso
Para ejecutar la herramienta podemos hacerlo de las siguientes formas:
```bash
# With the script copied to /usr/bin we can run it from any directory in the terminal
EvilQR.py
```
![imagen](https://user-images.githubusercontent.com/72285693/149815234-038273b7-a362-4002-87c4-084de3023ded.png)
   
or
```bash
# Running it directly from the tool's repository
python3 EvilQR.py
```
![imagen](https://user-images.githubusercontent.com/72285693/149814976-c27228b9-f130-43be-9de1-64de0a8d848c.png)

# DEMO

![demo](https://user-images.githubusercontent.com/72285693/149820249-0e9a07d8-b69b-4587-bab0-10c3a621ca5d.gif)

   
   
   
   
   
## Disclaimer
Cualquier acción y/o actividad relacionada con el material contenido en este sitio web es de su exclusiva responsabilidad. El uso indebido de esta herramienta puede dar lugar a la presentación de cargos penales contra las personas en cuestión. El autor de EvilQR no será responsable en caso de que se presenten cargos penales contra cualquier persona que haga un mal uso de la herramienta para infringir la ley.
