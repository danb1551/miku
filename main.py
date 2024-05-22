import subprocess
import time
import os
import colorama
from colorama import init, Fore, Back, Style

def hlavni_cast():
    print("")
    print(Style.RESET_ALL + "╔═════════════════════════════════════════════════════════════════════╗")
    print("║" + Fore.GREEN + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.MAGENTA + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.CYAN + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.RED + "......................." + Style.RESET_ALL + "Vítejte v YT-DOWNLOADER" + Fore.RED + "......................." + Style.RESET_ALL + "║")
    print("║" + Fore.GREEN + "............................." + Style.RESET_ALL + "Miluju tě!" + Fore.GREEN + ".............................." + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + "............................" + Style.RESET_ALL + "a fakt hodně." + Fore.BLUE + "............................" + Style.RESET_ALL + "║")
    print("║" + Fore.MAGENTA + "......................" + Style.RESET_ALL + "A určitě s tebou zůstanu," + Fore.MAGENTA + "......................" + Style.RESET_ALL + "║")
    print("║" + Fore.CYAN + "....................." + Style.RESET_ALL + "pokud se mnou zůstaneš i ty." + Fore.CYAN + "...................." + Style.RESET_ALL + "║")
    print("║" + Fore.RED + ".................." + Style.RESET_ALL + " \U0001F600" + " né, že s tím budeš zlobit " + "\U0001F600 " + Fore.RED + ".................." + Style.RESET_ALL + "║")
    print("║" + Fore.GREEN + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.MAGENTA + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.CYAN + "....................................................................." + Style.RESET_ALL + "║")
    print("╠═════════════════════════════════════════════════════════════════════╝")

def nacitani_procenta():
    procenta = 0
    for i in range(0, 101):
        procenta = procenta + 1
        time.sleep(0.1)
        os.system("cls")
        if procenta >= 0 and procenta <= 4.9:
            print(f"[                   ] {procenta}%")
        if procenta >= 5 and procenta <= 9.9:
            print(f"[=                  ] {procenta}%")
        if procenta >= 10 and procenta <= 14.9:
            print(f"[==                 ] {procenta}%")
        if procenta >= 15 and procenta <= 19.9:
            print(f"[===                ] {procenta}%")
        if procenta >= 20 and procenta <= 24.9:
            print(f"[====               ] {procenta}%")
        if procenta >= 25.01 and procenta <= 29.9:
            print(f"[=====              ] {procenta}%")
        if procenta == 25:
            print(f"[=====              ] {procenta}%")
            time.sleep(0.75)
        if procenta >= 30 and procenta <= 34.9:
            print(f"[======             ] {procenta}%")
        if procenta >= 35 and procenta <= 39.9:
            print(f"[=======            ] {procenta}%")
        if procenta >= 40.01 and procenta <= 44.9:
            print(f"[========           ] {procenta}%")
        if procenta == 40:
            print(f"[========           ] {procenta}%")
            time.sleep(0.75)
        if procenta >= 45 and procenta <= 49.9:
            print(f"[=========          ] {procenta}%")
        if procenta >= 50 and procenta <= 54.9:
            print(f"[==========         ] {procenta}%")
        if procenta >= 55 and procenta <= 59.9:
            print(f"[===========        ] {procenta}%")
        if procenta >= 60 and procenta <= 64.9:
            print(f"[============       ] {procenta}%")
        if procenta >= 65 and procenta <= 69.9:
            print(f"[=============      ] {procenta}%")
        if procenta >= 70 and procenta <= 74.9:
            print(f"[==============     ] {procenta}%")
        if procenta >= 75 and procenta <= 79.9:
            print(f"[===============    ] {procenta}%")
        if procenta >= 80.01 and procenta <= 84.9:
            print(f"[================   ] {procenta}%")
        if procenta == 80:
            print(f"[================   ] {procenta}%")
            time.sleep(0.75)
        if procenta >= 85 and procenta <= 89.9:
            print(f"[=================  ] {procenta}%")
        if procenta >= 90 and procenta <= 94.9:
            print(f"[================== ] {procenta}%")
        if procenta >= 95 and procenta <= 99.9:
            print(f"[================== ] {procenta}%")
        if procenta == 100:
            print(f"[===================] {procenta}%")
            time.sleep(0.25)

def vycistit():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def nacitani():
    nacteni1 = "...../"
    nacteni2 = ".....-"
    nacteni3 = ".....|"
    print("Loading" + nacteni1)
    time.sleep(0.25)
    vycistit()
    print("Loading" + nacteni2)
    time.sleep(0.25)
    vycistit()
    print("Loading" + nacteni3)
    time.sleep(0.25)
    vycistit()
    print("Loading" + nacteni1)
    time.sleep(0.25)
    vycistit()
    print("Loading" + nacteni2)
    time.sleep(0.25)
    vycistit()
    print("Loading" + nacteni3)
    time.sleep(0.25)
    vycistit()
    print("Loading" + nacteni1)
    time.sleep(0.25)
    vycistit()
    print("Loading" + nacteni2)
    time.sleep(0.25)
    vycistit()
    print("Loading" + nacteni3)
    time.sleep(0.25)
    vycistit()
    print("Loading" + nacteni1)
    time.sleep(0.25)
    vycistit()
    print("Loading" + nacteni2)
    time.sleep(0.25)
    vycistit()
    print("Loading" + nacteni3)
    time.sleep(0.25)
    vycistit()
