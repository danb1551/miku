import subprocess
import time
import os
import colorama
from colorama import init, Fore, Back, Style
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import psutil
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
import winreg

list_aplikace = []
list_muzika = []

def hlavni_cast():
    print("")
    print(Style.RESET_ALL + "╔═════════════════════════════════════════════════════════════════════╗")
    print("║" + Fore.GREEN + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.MAGENTA + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.CYAN + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.RED + "............................" + Style.RESET_ALL + "Modern" + Fore.RED + "..................................." + Style.RESET_ALL + "║")
    print("║" + Fore.GREEN + "............................" + Style.RESET_ALL + "Innovative" + Fore.GREEN + "..............................." + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + "............................" + Style.RESET_ALL + "Knowledgeable" + Fore.BLUE + "............................" + Style.RESET_ALL + "║")
    print("║" + Fore.MAGENTA + "............................" + Style.RESET_ALL + "Unique" + Fore.MAGENTA + "..................................." + Style.RESET_ALL + "║")
    print("║" + Fore.CYAN + "............................" + Style.RESET_ALL + "MIKU" + Fore.CYAN + "....................................." + Style.RESET_ALL + "║")
    print("║" + Fore.RED + "..............." + Style.RESET_ALL + " \U0001F600" + " Do you masturbate to her picture? " + "\U0001F600 " + Fore.RED + "............." + Style.RESET_ALL + "║")
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

def volume_up(change):
    increment = change / 100.0
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = min(current_volume + increment, 1.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    print(f"Volume increased to {new_volume * 100:.0f}%")

def volume_down(change):
    decrement = change / 100.0
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = max(current_volume - decrement, 0.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    print(f"Volume decreased to {new_volume * 100:.0f}%")

def get_system_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    return current_volume * 100

def get_audio_sessions():
    sessions = AudioUtilities.GetAllSessions()
    audio_info = []
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        process = session.Process
        if process:
            process_name = process.name()
            process_id = process.pid
            audio_info.append({
                "process_name": process_name,
                "process_id": process_id,
                "volume": volume.GetMasterVolume() * 100
            })
    return audio_info

def get_installed_apps():
    uninstall_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
    installed_apps = []
    # Získání aplikací nainstalovaných pro všechny uživatele
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, uninstall_key) as key:
        for i in range(winreg.QueryInfoKey(key)[0]):
            subkey_name = winreg.EnumKey(key, i)
            with winreg.OpenKey(key, subkey_name) as subkey:
                try:
                    app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    installed_apps.append(app_name)
                except FileNotFoundError:
                    pass
    # Získání aplikací nainstalovaných pro aktuálního uživatele
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, uninstall_key) as key:
        for i in range(winreg.QueryInfoKey(key)[0]):
            subkey_name = winreg.EnumKey(key, i)
            with winreg.OpenKey(key, subkey_name) as subkey:
                try:
                    app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    installed_apps.append(app_name)
                except FileNotFoundError:
                    pass

    return installed_apps

installed_apps = get_installed_apps()
for app in installed_apps:
    list_aplikace.append(app)

prave_hraje = get_audio_sessions()
for pisnicky in prave_hraje:
    list_muzika.append(pisnicky)

with open('data_aplikace.dat', 'w') as file:
    aplikace = str(list_aplikace)
    file.write(aplikace)

with open('data_muzika.dat', 'w') as file:
    muzika = str(list_muzika)
    file.write(muzika)

#with open('data_aplikace.dat', 'w') as file:
#    file.write(list)



hlavni_cast()
time.sleep(2)
print("╠═ 1.) ")
print("╠═ 2.) ")
print("╠═ 3.) ")
print("╠═ 4.) ")
print("╠═ 5.) ")
print("╠═ 6.) ")
print("╠═ 7.) ")
print("╠═ 8.) ")
print("╠═ 9.) ")
print("╠═ 10.) ")
print("╠═ 11.) ")
print("╠═ 12.) ")
print("╠═ 13.) ")
print("╠═ 14.) ")
print("╠═ 15.) ")
print("╠═ 16.) ")
print("╠═ 17.) ")
print("╠═ 18.) ")
print("╠═ 19.) ")
print("╠═ 20.) ")
print("╠═ 21.) ")
print("╠═ 22.) ")
print("╠═ 23.) ")
print("╠═ 24.) ")
print("╠═ 25.) ")
print("╠═ 26.) ")
print("╠═ 27.) ")
print("╠═ 28.) ")
print("╠═ 29.) ")
print("╠═ 30.) ")
print("╚════>")
