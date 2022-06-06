#!/usr/bin/python3
import qrcode, signal, sys, argparse,os
from alive_progress import alive_bar
from time import sleep
from os import system
from requests import post
from urllib.parse import urlparse

# Colors
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Banner
system('clear')
banner =  style.RED + """
     7MMlllYMM            db   7MM    g8ll8q   7MMlllMq  
      MM     7                  MM  dP      YM  MM    MM 
      MM   d  7M     MF  7MM    MM dM        MM MM    M9  
      MMmmMM   VA    V    MM    MM MM        MM MMmmdM9  """ +style.RESET  + style.CYAN + """(by: """ + style.UNDERLINE +  """Harrizzon""" + style.RESET + style.CYAN + """)""" +  style.RED + """
      MM   Y    VA  V     MM    MM MM        MP MM  YM  
      MM      M  VVV      MM    MM  Mb      dP  MM    Mb 
     JMMmmmmMMM   W      JMML  JMML  llbmmdl   JMML   JMM
                                         MMb              
                                          bood    
""" + style.RESET


# Exit
def ctrl_c(sig, frame):
    system('clear')
    print(style.RED + "\n [!] Saliendo")
    sys.exit(0)
signal.signal(signal.SIGINT, ctrl_c)

def maskurl(main_url: str, mask_dom: str, keywords: str) -> str:
    furl = shortner(main_url)
    return f"{mask_dom}-{keywords}@{urlparse(furl).netloc + urlparse(furl).path}"

def shortner(b_url: str) -> str:
    return post(f"https://is.gd/create.php?format=json&url={b_url}").json()['shorturl']

pwd = os.getcwd()

# MAIN
if __name__ == '__main__':
    print(banner)

    if len(sys.argv) == 1:
        main_url = input(style.WHITE + "Enter an URL (With " + style.CYAN + "http " + style.WHITE +  "or " + style.CYAN + "https" + style.WHITE + "):\n" + style.CYAN)
        while True:
            if len(main_url) == 0:
                system('clear')
                print(style.RED + "[!] Empty URL - Run the tool again [!]")
                sys.exit(1)

            choose_mask = input(style.YELLOW + "\n¿do you want to mask the url? " + style.GREEN + "(y/n)\n" + style.GREEN)
            if choose_mask == "n":
                system('clear')
                qr = qrcode.QRCode(
                version=4,
                box_size=10,
                border=1
                )
                qr.add_data(main_url)
                qr.make(fit=True)
                img = qr.make_image(fill='black', back_color='white')
                print(style.YELLOW + "\nGenerating QR Code\n" + style.RESET)
            
            # QR GENERATING
                with alive_bar(100, spinner='pulse') as progrs:

                    for i in range(100):
                        sleep(0.01)
                        progrs()
                system('clear')        
                print(style.GREEN + "\n\n[>] QR Generado con exito [<]" + style.RESET)
                print(style.GREEN + "QR stored in the directory: " + style.RESET + style.CYAN + pwd + style.RESET)
                sleep(4)
                img.save('eQRCode.png')
                sys.exit(0)
            if choose_mask == "y":
                system('clear')
                print(style.RED + "\n[!] " +style.UNDERLINE + style.YELLOW + "Masking the next URL" + style.RESET + style.RED + " >> " + style.CYAN + main_url + "\n")
                mask_dom = input(style.WHITE + "\nEnter the domain name to mask the URL (With " + style.CYAN + style.UNDERLINE +  "http" + style.RESET + style.WHITE + " or " + style.CYAN + style.UNDERLINE + "https" + style.RESET + style.WHITE +  " ex: " + style.CYAN + style.UNDERLINE + "https://" + style.RESET + style.WHITE + "facebook.com <> " + style.CYAN + style.UNDERLINE + "http://" + style.RESET + style.WHITE + "google.com): \n" + style.CYAN)
                keywords = input(style.WHITE + "\nEnter the keywords without whitespace (Use " + style.CYAN + "'-' " + style.WHITE + "ex: free" + style.CYAN + "-"+ style.WHITE + "money): \n" + style.CYAN)
                f_url = maskurl(main_url, mask_dom, keywords)
                print("\n" + style.WHITE + "This is your masked URL >> " + style.MAGENTA + f_url)
                qr = qrcode.QRCode(
                version=4,
                box_size=10,
                border=1
                )
                qr.add_data(f_url)
                qr.make(fit=True)
                img = qr.make_image(fill='black', back_color='white')
                print(style.YELLOW + "\nGenerating QR Code\n" + style.RESET)
                sleep(3)
            # QR GENERATING
                with alive_bar(100, spinner='pulse') as progrs:

                    for i in range(100):
                        sleep(0.01)
                        progrs()
                system('clear')
                print(style.GREEN + "\n\n[>] QR Successfully Generated [<]" + style.RESET)
                print(style.GREEN + "QR stored in the directory: " + style.RESET + style.CYAN + pwd + style.RESET)
                sleep(4)
                img.save('eQRCode.png')
                sys.exit(0)
                


            else:
                system('clear')
                print(style.RED + "\n [!] Please enter a valid option" + style.RESET)
                sleep(2)
                system('clear')
    else:
        print(style.RED + "[!]" + style.WHITE + "Invalid Argument" + style.RESET)
        sys.exit(1)
