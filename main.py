import scr.parsers as parsers
import colorama
import os
import json
import socket
import subprocess
import asyncio
import scr.ui as ui
from pyngrok import ngrok
import random as rnd
from pathlib import Path


page = "main"

colorama.init()


class func:
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

        elif choice == "1":
            serversList = os.listdir(settings["Servers_dir"])
            ui.my_servers()
            for i in range(0, len(serversList)):
                print(f"{i+1} - {serversList[i]}")

            print(colorama.Fore.GREEN)
            choice = int(input("> ")) - 1
            print(colorama.Style.RESET_ALL)

            serverName = serversList[int(choice)]
            serverDir = f'{settings["Servers_dir"]}/{serverName}'

            ngrokStarted = False
            ftpStarted = False
            mcStarted = False
            firstLaunch = False
            tunnels = ""

            instant_settings = {}

            with open(f"{serverDir}/settings.json") as f:
                instant_settings = json.load(f)

            gid = rnd.randint(00000, 99999)

            server_properties = {}
            server_properties_args_ids = []
            if os.path.exists(f'{serverDir}/server.properties'):
                with open(f'{serverDir}/server.properties', 'r') as f:
                    file = f.read().split('\n')
                    for i in file:
                        if '=' in i:
                            server_properties[i.split('=')[0]] = i.split('=')[1]


                for i, j in enumerate(server_properties):
                    server_properties_args_ids.append(j)

            while True:
                ls_screen_dir = os.listdir('/data/data/com.termux/files/home/.screen')

                if ls_screen_dir == []:
                    screen_pid = ''
                    mcStarted = False

                else:
                    for i in ls_screen_dir:
                        file_name = ''.join(i.split(' ')[-1:])
                        print(file_name.split('.'))

                        if file_name.split('.')[1] == f'mcServer_{gid}':
                            screen_pid = file_name.split('.')[0]
                            mcStarted = True
                        else:
                            mcStarted = False


                page = "server_menu"
                tcp_tunnel = ""
                ui.clear()
                ui.Server_menu()
                print(
                    rf"""
1 - {'Return to' if mcStarted == True else "Start"} minecraft server
2 - {"Stop" if ftpStarted == True else "Start"} ftp server
3 - {"Stop" if ngrokStarted == True else "Start"} ngrok 
4 - Instant settings
{"5 - Eula true (coming soon)" if os.path.exists(f'{serverDir}/eula.txt') else ''}
{"6 - server.properties editor" if os.path.exists(f'{serverDir}/server.properties') else ''}
{"7 - Apply settings to server.properties" if os.path.exists(f'{serverDir}/server.properties') else ''}
0 - Exit

{f"{func.getLocalIP()}:{settings['FTP_port']} to connect to ftp server" if ftpStarted else f" "}
{f"Ngrok: {tunnels[0]}" if ngrokStarted else f" "}

{"stop minecraft server: ctrl + a + k (in session)" if mcStarted == True else ""}

                        """
                )

                print(colorama.Fore.GREEN)
                choice = input("> ")
                print(colorama.Style.RESET_ALL)
                ui.clear()

                if choice == "0":
                    os.system(f"sv down {serverName}-ftpd")
                    os.system(
                        "kill $(ps aux | grep '[p]ython -m pyftpdlib' | awk '{print $2}')"
                    )
                    if mcStarted == True:
                        os.system(f'kill {screen_pid}')
                    ngrok.kill()
                    ui.clear()
                    page = "main"
                    ui.main_menu()
                    break

                elif choice == "1":
                    if mcStarted == False:
                        ui.clear()
                        print('Stop server: ctrl a + k')
                        print('Minimize server: ctrl a + d')
                        print('Press enter to continue')
                        input()
                        javaExec = ''
                        if instant_settings["jdkVer"] == 8:
                            javaExec = '/usr/lib/jvm/java-8-openjdk-arm64/jre/bin/java'
                        elif instant_settings["jdkVer"] == 17:
                            javaExec = '/usr/lib/jvm/java-17-openjdk-arm64/bin/java'

                        subprocess.run(
                            [
                            "screen",
                            "-dmS",
                            f"mcServer_{gid}"
                            ]
                        )
                        os.system(fr'screen -S mcServer_{gid} -X stuff "proot-distro login ubuntu --bind {settings["Servers_dir"]}:/root/servers\n"')
                        os.system(fr'screen -S mcServer_{gid} -X stuff "update-alternatives --set java {javaExec} && cd /root/servers/{serverName} && java -Xms{instant_settings["Xms"]}m -Xmx{instant_settings["Xmx"]}m {instant_settings["Exec"]}\n"')

                        subprocess.run([
                            "screen",
                            "-r",
                            f"mcServer_{gid}"
                        ])
                    else:
                        subprocess.run(["screen", "-r", f"mcServer_{gid}"])

                elif choice == "2":
                    if ftpStarted == False:

                        subprocess.run(["sv", "up", f"{serverName}-ftpd"])
                        ftpStarted = True
                    else:
                        subprocess.run(["sv", "down", f"{serverName}-ftpd"])
                        os.system(
                            "kill $(ps aux | grep '[p]ython -m pyftpdlib' | awk '{print $2}')"
                        )
                        ftpStarted = False
                    ui.clear()

                elif choice == "3":
                    if ngrokStarted == False:

                        ngrok.set_auth_token(settings["ngrok_authtoken"])
                        tcp_tunnel = ngrok.connect(
                            settings["Standart_server_port"], "tcp"
                        )
                        tunnels = ngrok.get_tunnels()
                        ngrokStarted = True
                    else:

                        ngrok.kill()
                        ngrok.disconnect(tcp_tunnel)
                        ngrokStarted = False
                    ui.clear()

                elif choice == "4":
                    while True:
                        ui.settings_menu()
                        print(f"1 - Min server RAM: {instant_settings['Xms']} in megabytes")
                        print(f"2 - Max server RAM: {instant_settings['Xmx']} in megabytes")
                        print(f"3 - OpenJDK version: {instant_settings['jdkVer']}")
                        print(f"4 - Server port: {instant_settings['Port']}")
                        print(f"5 - Server port: {instant_settings['Online_mode']}")
                        print(f"0 - Back\n\n\n\n")

                        print(colorama.Fore.GREEN)
                        choice = input("> ")
                        print(colorama.Style.RESET_ALL)

                        if choice == "0":
                            os.system(f"rm -rf {serverDir}/settings.json")
                            with open(f"{serverDir}/settings.json", "w") as f:
                                json.dump(settings, f)
                            ui.clear()
                            break
                        elif choice not in "12345" or choice == "":
                            continue

                        else:
                            print(colorama.Fore.GREEN)
                            variable = input("> ")
                            print(colorama.Style.RESET_ALL)
                            if choice in "12345":
                                match choice:
                                    case "1":
                                        instant_settings["Xms"] = variable
                                    case "2":
                                        instant_settings["Xmx"] = variable
                                    case "3":
                                        instant_settings["jdkVer"] = variable
                                    case "4":
                                        instant_settings["Port"] = variable
                                    case "5":
                                        instant_settings["Online_mode"] = variable

                                ui.clear()
                                continue

                elif choice == "5":
                    if settings["Server_eula"] == "True":
                        eula = f"#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://aka.ms/MinecraftEULA).\n#Wed Feb 08 08:56:25 GMT 2023\neula=true"
                        with open(f'{serverDir}/eula.txt', 'w') as file:
                            file.write(eula)
                    else:
                        print('Set eula to True in settings')


                elif choice == "6":
                    if os.path.exists(f'{serverDir}/server.properties'):
                        while True:
                            ui.clear()
                            ui.Properties_menu()
                            print('     {id} - {argument}={value}\n'
                                  '     input: id value\n')
                            for i, j in enumerate(server_properties):
                                print(f'{i + 1} - {j}={server_properties[j]}')

                            print('\n0 - exit')

                            inp = input('>')
                            if inp == '0':

                                out = f''
                                for i, j in enumerate(server_properties):
                                    out += f'{j}={server_properties[j]}\n'
                                with open(f'{serverDir}/server.properties', 'w') as f:
                                    f.write(out[:-1])
                                break

                            inp = inp.split(' ')
                            server_properties.update({server_properties_args_ids[int(inp[0]) - 1]: inp[1]})

                        with open(f'{serverDir}/server.properties', 'r') as f:
                            file = f.read().split('\n')
                            for i in file:
                                server_properties[i.split('=')[0]] = i.split('=')[1]

                        for i, j in enumerate(server_properties):
                            server_properties_args_ids.append(j)
                        else:
                            print('server.properties doesn`t exists')

                elif choice == "7":
                    server_properties['query.port'] = instant_settings["Port"]
                    server_properties['online-mode'] = instant_settings["Online_mode"]
                    for i, j in enumerate(server_properties):
                        out += f'{j}={server_properties[j]}\n'
                    with open(f'{serverDir}/server.properties', 'w') as f:
                        f.write(out[:-1])

        elif choice == "2":
            page = "choice version"

            ui.clear()
            ui.Core_menu()

            print(colorama.Fore.GREEN)
            choiceCore = input("> ")
            print(colorama.Style.RESET_ALL)
            ui.clear()

            vanila = parsers.vanilla()
            out = []

            for j, i in enumerate(vanila):
                ass = i.split(".")
                if int(ass[1]) >= 5:
                    out.append(vanila[int(j)])

            out = list(reversed(out))

            ui.clear()
            ui.VersionMenu()
            for j, i in enumerate(out):
                print(f"{j + 1} - {out[int(j)]}")

            print(colorama.Fore.GREEN)
            inputVersion = int(input("> ")) - 1
            version = out[inputVersion]
            print(colorama.Style.RESET_ALL)

            ui.clear()

            download_link = ""

            if choiceCore == "1":
                download_link = parsers.vanilla(version)
            elif choiceCore == "2":
                download_link = parsers.forge(version)
            elif choiceCore == "3":
                download_link = parsers.spigot(version)
            elif choiceCore == "4":
                download_link = parsers.fabric()
            ui.server_name()

            print(colorama.Fore.GREEN)
            name = input("> ")
            print(colorama.Style.RESET_ALL)

            if os.path.exists(settings["Servers_dir"]):
                pass
            else:
                os.system(f"mkdir {settings['Servers_dir']}")

            os.system(f'mkdir {settings["Servers_dir"]}/{name}')

            jdkVer = ""

            if version.split(".")[1] <= "16":
                jdkVer = 8
            elif version.split(".")[1] >= "17":
                jdkVer = 17



            os.system(f"mkdir /data/data/com.termux/files/usr/var/service/{name}-ftpd")
            os.system(
                f"touch /data/data/com.termux/files/usr/var/service/{name}-ftpd/run.sh"
            )

            if choiceCore == "1" or choiceCore == "3":
                print("Wait...")
                os.system(
                    f'wget {download_link} -O {settings["Servers_dir"]}/{name}/server.jar'
                )
                os.system("rm -rf server.jar")
            elif choiceCore == "2":
                os.system(
                    f'wget {download_link} -O {settings["Servers_dir"]}/{name}/forge_installer.jar'
                )
                os.system(f'cd {settings["Servers_dir"]}/{name} && java -jar forge_installer.jar --installServer')
                os.system(f'rm -rf {settings["Servers_dir"]}/{name}/forge_installer.jar')
                os.system(f'mv {settings["Servers_dir"]}/{name}/forge*.jar {settings["Servers_dir"]}/{name}/server.jar')

            elif choiceCore == "4":
                os.system(
                    f'wget {download_link} -O {settings["Servers_dir"]}/{name}/fabric_installer.jar'
                )
                os.system(f'java -jar {settings["Servers_dir"]}/{name}/fabric_installer.jar server -dir {settings["Servers_dir"]}/{name} -mcversion {version} -downloadMinecraft')
                os.system(f'rm -rf {settings["Servers_dir"]}/{name}/fabric_installer.jar')
                os.system(f'mv {settings["Servers_dir"]}/{name}/server.jar {settings["Servers_dir"]}/{name}/vanilla.jar')
                os.system(f'mv {settings["Servers_dir"]}/{name}/fabric-server-launch.jar {settings["Servers_dir"]}/{name}/server.jar')
                os.system(f'echo "serverJar=vanilla.jar" > {settings["Servers_dir"]}/{name}/fabric-server-launcher.properties')

            Exec = '-jar server.jar'
            ls_server_dir = os.listdir(f'{settings["Servers_dir"]}/{name}')

            if choiceCore == '2':
                for i in ls_server_dir:
                    if i == 'run.sh':
                        with open(f'{settings["Servers_dir"]}/{name}/run.sh', 'r') as f:
                            for i in f.read()[:-1].split('\n'):
                                if i[0] != '#':
                                    Exec = i.split(' ')[2]
                                    break



            instant_settings = {
                "Xmx": settings["Xmx"],
                "Xms": settings["Xms"],
                "jdkVer": jdkVer,
                "Port": settings["Standart_server_port"],
                "Online_mode": settings['default_online_mode'],
                "Core": choiceCore,
                "Version": version,
                "Exec": Exec
            }

            os.system(f'touch {settings["Servers_dir"]}/{name}/settings.json')
            with open(f'{settings["Servers_dir"]}/{name}/settings.json', "w") as f:
                json.dump(instant_settings, f)

            with open(
                f"/data/data/com.termux/files/usr/var/service/{name}-ftpd/run.sh", "w"
            ) as f:
                f.write(
                    f"#!/data/data/com.termux/files/usr/bin/sh \npython -m pyftpdlib -p {settings['FTP_port']} -d {settings['Servers_dir']}/{name} -w"
                )

            os.system(
                f"mv /data/data/com.termux/files/usr/var/service/{name}-ftpd/run.sh /data/data/com.termux/files/usr/var/service/{name}-ftpd/run"
            )
            os.system(
                f"chmod +x /data/data/com.termux/files/usr/var/service/{name}-ftpd/run"
            )
            os.system(f"mkdir $PREFIX/var/service/{name}-ftpd/log")
            os.system(
                f"ln -sf $PREFIX/share/termux-services/svlogger $PREFIX/var/service/{name}-ftpd/log/run"
            )
            page = "main"
            ui.clear()
            ui.main_menu()

        elif choice == "3":
            serversList = os.listdir(settings["Servers_dir"])
            ui.Delete_menu()
            for i in range(0, len(serversList)):
                print(f"{i + 1} - {serversList[i]}")

            print("0 - exit")

            print(colorama.Fore.GREEN)
            try:
                choice = int(input("> ")) - 1
            except:
                continue
            print(colorama.Style.RESET_ALL)

            try:
                serverName = serversList[int(choice)]
            except:
                continue

            if choice == "0":
                ui.clear()
                page = "main"
                ui.main_menu()
                break

            else:
                os.system(f"rm -rf {settings['Servers_dir']}/{serverName}")
                os.system(f"rm -rf $SVDIR/{serverName}-ftpd")
                ui.clear()
                page = "main"
                ui.main_menu()

        elif choice == "4":
            page = "settings"
            while True:
                ui.settings_menu()
                ui.clear()
                print(
                    f"1 - Standart minecraft server port: {settings['Standart_server_port']}"
                )
                print(f"2 - FTP port: {settings['FTP_port']}")
                print(f"3 - Servers dir: {settings['Servers_dir']}")
                print(f"4 - Server eula: {settings['Server_eula']} (coming soon)")
                print(f"5 - Min server RAM: {settings['Xms']} in megabytes")
                print(f"6 - Max server RAM: {settings['Xmx']} in megabytes")
                print(
                    f"7 - Ngrok authtoken(see in README.md): {settings['ngrok_authtoken']}"
                )
                print(f"8 - Default online mode: {settings['default_online_mode']}")
                print(f"0 - Back\n\n\n\n")

                print(colorama.Fore.GREEN)
                choice = input("> ")
                print(colorama.Style.RESET_ALL)

                if choice == "0":
                    os.system("rm -rf settings.json")
                    with open("settings.json", "w") as f:
                        json.dump(settings, f)
                    ui.clear()
                    page = "main"
                    ui.main_menu()
                    break

                elif choice not in "12345678" or choice == "":
                    continue

                else:
                    print(colorama.Fore.GREEN)
                    variable = input("> ")
                    print(colorama.Style.RESET_ALL)
                    if choice in "12345678":
                        match choice:
                            case "1":
                                settings["Standart_server_port"] = variable
                            case "2":
                                settings["FTP_port"] = variable
                            case "3":
                                settings["Servers_dir"] = variable
                            case "4":
                                settings["Server_eula"] = variable
                            case "5":
                                settings["Xms"] = variable
                            case "6":
                                settings["Xmx"] = variable
                            case "7":
                                settings["ngrok_authtoken"] = variable
                            case "8":
                                settings['default_online_mode'] = variable
                        ui.clear()
                        continue

        elif choice == "5":
            page = "main"
            ui.main_menu()
            print(f"Version: {settings['App_version']}")

        elif choice == "6":
            ui.clear()
            os.system('screen -dmS mcserver_install')
            os.system('screen -S mcserver_install -X stuff "proot-distro login ubuntu --bind "${PWD}"/proot_scr:/root; exit\n"')
            os.system('screen -S mcserver_install -X stuff "chmod 777 update_java.sh && ./update_java.sh; exit\n"')
            os.system('screen -r mcserver_install')

        elif choice == "0":
            exit(1)
