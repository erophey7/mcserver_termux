import scr.parsers as parsers
import colorama
import os
import time
import json
import socket
import subprocess
import asyncio
import scr.ui as ui
import multiprocessing
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer



page = "main"

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


def runFTP(ftpDir):
    authorizer = DummyAuthorizer()
    authorizer.add_anonymous(ftpDir, perrm=('r', 'w'))
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer((func.getLocalIP(), settings['FTP_port']), handler)
    server.serve_forever()


settings = func.readSettings()

ui.clear()
ui.main_menu()


serverStarted = False
ngrokStarted = False
ftpStarted = False

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

        elif choice == "1":
            serversList = os.listdir(settings["Servers_dir"])
            ui.my_servers()
            for i in range(0, len(serversList)):
                print(f'{i+1} - {serversList[i]}')

            print(colorama.Fore.GREEN)
            choice = int(input("> "))-1
            print(colorama.Style.RESET_ALL)


            serverDir = f'{settings["Servers_dir"]}/{serversList[int(choice)]}'

            while True:
                page = 'server_menu'
                ui.clear()
                ui.Server_menu()
                print(fr'''
1 - {"Stop" if serverStarted == True else "Start"} minecraft server
2 - {"Stop" if ftpStarted == True else "Start"} ftp server
3 - {"Stop" if ngrokStarted == True else "Start"} ngrok
0 - Exit

{f"{func.getLocalIP()}:{settings['FTP_port']} to connect to ftp server" if ftpStarted else f" "}

                        ''')

                print(colorama.Fore.GREEN)
                choice = input("> ")
                print(colorama.Style.RESET_ALL)
                ui.clear()

                FTPProc = multiprocessing.Process(target=runFTP(serverDir))

                if choice == '0':
                    os.system('pkill java && pkill ftpd && pkill ngrok')
                    page = 'main_manu'
                    break

                elif choice == '1':
                    pass

                elif choice == '2':
                        if ftpStarted == False:

                            FTPProc.start()
                            ftpStarted = True
                        else:
                            FTPProc.close()
                            ftpStarted = False




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
            vanila_link = vanila[versionNumber][1]
            ui.clear()
            ui.Core_menu()




            print(colorama.Fore.GREEN)
            choiceCore = input("> ")
            print(colorama.Style.RESET_ALL)

            download_link = ''

            if choiceCore == "1":
                download_link = vanila_link

            ui.clear()
            ui.server_name()

            print(colorama.Fore.GREEN)
            name = input("> ")
            print(colorama.Style.RESET_ALL)


            if os.path.exists(settings['Servers_dir']):
                pass
            else:
                os.system(f"mkdir {settings['Servers_dir']}")

            os.system(f'cp -r ServerExample {settings["Servers_dir"]}/{name}')
            if choiceCore != "2":
                print("Wait...")
                os.system(f'wget -c {download_link} -o {settings["Servers_dir"]}/{name}/server.jar')
            else:
                pass

            with open(f'{settings["Servers_dir"]}/{name}/startFTP.sh', 'w') as f:
                f.write(f"busybox tcpsvd -vE 0.0.0.0 {settings['FTP_port']} busybox ftpd -w {settings['Servers_dir']}/{name}")

            os.system(f'chmod +x {settings["Servers_dir"]}/{name}/startFTP.sh')

            page = "main"
            ui.clear()
            ui.main_menu()

        elif choice == "3":
            pass

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

        elif choice == "5":
            page = "main"
            ui.main_menu()
            print(f"Version: {settings['App_version']}")

        elif choice == "0":
            exit(0)