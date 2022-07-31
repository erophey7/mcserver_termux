import scr.parsers as parsers
import colorama
import os
import time
import json
import socket
import subprocess
import asyncio
import scr.ui as ui




page = "main"


rowAni = (">", " ")
rowAniFrame = 0

colorama.init()



class func:

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
        with open("settings.json") as f:
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

    if page == "main":
        if choice == "":
            page = "main"
            ui.main_menu()

        elif choice == "2":
            page = "choice version"
            ui.clear()
            ui.VersionMenu()
            vanila = asyncio.run(parsers.vanilaParser())
            for j, i in enumerate(vanila):
                print(f'{j+1} - {i[0]}')


            print(colorama.Fore.GREEN)
            inputVersion = int(input("> "))-1
            version = vanila[inputVersion][0]
            versionNumber = inputVersion
            print(colorama.Style.RESET_ALL)

            ui.clear()
            ui.Core_menu()

            print(colorama.Fore.GREEN)
            choiceCore = input("> ")
            print(colorama.Style.RESET_ALL)

            download_link = ''

            if choiceCore in "123":
                match choice:
                    case "1":
                        download_link = vanila[versionNumber][1]

            print(version)
            print(download_link)

            ui.clear()
            ui.server_name()

            print(colorama.Fore.GREEN)
            name = input("> ")
            print(colorama.Style.RESET_ALL)


            if os.path.exists(settings['Servers_dir']):
                os.system(f'cp ServerExample {settings["Servers_dir"]}/{name}')
                if choiceCore != "2":
                    os.system(f'wget -c {download_link} -o server.jar')
                else:
                    pass
            else:
                os.system(f"mkdir {settings['Servers_dir']}")






        elif choice == "4":
            page = "settings"
            while True:
                ui.settings_menu()
                ui.clear()
                print(f"1 - Standart minecraft server port: {settings['Standart_server_port']}")
                print(f"2 - Auto start FTP server after start minecraft server: {settings['Auto_start_FTP_server']}")
                print(f"3 - FTP port: {settings['FTP_port']}")
                print(f"4 - Servers dir: {settings['Servers_dir']}")
                print(f"5 - Server eula: {settings['Server_eula']}")
                print(f"6 - Min server RAM: {settings['Xms']} in megabytes")
                print(f"7 - Max server RAM: {settings['Xmx']} in megabytes")
                print(f"0 - Back\n\n\n\n")

                print(colorama.Fore.GREEN)
                choice = input("> ")
                print(colorama.Style.RESET_ALL)

                if choice == "0":
                    os.system('del settings.json')
                    with open("settings.json", "rw") as f:
                        json.dump(settings, f)
                    ui.clear()
                    page = "main"
                    ui.main_menu()
                    break

                elif choice not in "1234567" or choice == "":
                    continue

                else:
                    print(colorama.Fore.GREEN)
                    variable = input("> ")
                    print(colorama.Style.RESET_ALL)
                    if choice in '1234567':
                        match choice:
                            case "1":
                                settings['Standart_server_port'] = variable
                            case "2":
                                settings['Auto_start_FTP_server'] = variable
                            case "3":
                                settings['FTP_port'] = variable
                            case "4":
                                settings['Servers_dir'] = variable
                            case "5":
                                settings['Server_eula'] = variable
                            case "6":
                                settings['Xms'] = variable
                            case "7":
                                settings['Xmx'] = variable
                        ui.clear()
                        continue

        elif choice == "6":
            page = "main"
            ui.main_menu()
            print(f"Version: {settings['App_version']}")

        elif choice == "0":
            exit(0)