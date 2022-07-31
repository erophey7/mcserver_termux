
import colorama
import os
import time
import json
import socket
import subprocess


soft_version = 0.1


page = "main"


rowAni = (">", " ")
rowAniFrame = 0

colorama.init()


class ui():


    def clear():

        if os.name == 'nt':
             _ = os.system('cls')


        else:
             os.system('clear')

    def main_menu():
        print()
        print(colorama.Fore.GREEN + "                  _________                                 \n",
                                    "   _____   ____  /   _____/ ______________  __ ___________  \n",
                                    "  /     \_/ ___\ \_____  \_/ __ \_  __ \  \/ // __ \_  __ \ \n",
                                    " |  Y Y  \  \___ /        \  ___/|  | \/\   /\  ___/|  | \/ \n",
                                    " |__|_|  /\___  >_______  /\___  >__|    \_/  \___  >__|    \n",
                                    "       \/     \/        \/     \/                 \/        \n")
        print(colorama.Style.RESET_ALL)
        print(" 1 - My servers\n",
              "2 - Create server\n",
              "3 - Delete server\n",
              "4 - Settings\n",
              "5 - Check version\n",
              "0 - Exit \n\n\n\n\n\n")



class func():

    def vanilaParser():
        pass


    def getLocalIP():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip


    def readSettings():
        settings = {}
        with open("../settings.json") as f:
            settings = json.load(f)
        return settings


settings = func.readSettings()

ui.clear()
ui.main_menu()


while True:
    choice = ""
    print(colorama.Fore.GREEN)
    choice = input("> ")
    print(colorama.Style.RESET_ALL)
    ui.clear()
    time.sleep(0.05)

    if page == "main":
        if choice == "":
            page = "main"
            ui.main_menu()

        elif choice == "4":
            page = "settings"
            ui.clear()
            print(f"1 - Standart minecraft server port: {settings['Standart_server_port']}")
            print(f"2 - Auto start FTP server after start minecraft server: {settings['Auto_start_FTP_server']}")
            print(f"3 - FTP port: {settings['FTP_port']}")
            print(f"4 - Servers dir: {settings['Servers_dir']}")
            print(f"5 - Server eula: {settings['Server_eula']}")
            print(f"0 - Back")


        elif choice == "6":
            page = "main"
            ui.main_menu()
            print(f"Version: {soft_version}")

        elif choice == "0":
            exit(0)

