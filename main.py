
import colorama
import os
import time


page = ""

clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

rowAni = (">", " ")
rowAniFrame = 0

colorama.init()


class ui():

    def clear():

        if os.name == 'nt':
             _ = os.system('cls')


        else:
             _ = os.system('clear')

    def main_menu():
        page = "main"
        print()
        print(colorama.Fore.GREEN + "                  _________                                 ")
        print(colorama.Fore.GREEN + "   _____   ____  /   _____/ ______________  __ ___________  ")
        print(colorama.Fore.GREEN + "  /     \_/ ___\ \_____  \_/ __ \_  __ \  \/ // __ \_  __ \ ")
        print(colorama.Fore.GREEN + " |  Y Y  \  \___ /        \  ___/|  | \/\   /\  ___/|  | \/ ")
        print(colorama.Fore.GREEN + " |__|_|  /\___  >_______  /\___  >__|    \_/  \___  >__|    ")
        print(colorama.Fore.GREEN + "       \/     \/        \/     \/                 \/        ")
        print(colorama.Style.RESET_ALL)
        print("1 - My servers")
        print("2 - Create server")
        print("3 - Delete server")
        print("4 - Settings")
        print("5 - Setup required packages")
        print("0 - exit")
        print(f"\n\n\n\n\n")


class functions():
    

    def exit():
        exit
        


ui.main_menu()



while True:
    choice = ""
    print(colorama.Fore.GREEN)
    choice = input("> ")
    print(colorama.Style.RESET_ALL)
    print(clear)
    time.sleep(0.05)
    if page == "main":
        if choice == "":
            ui.main_menu()
        
        elif choice == "0":
            exit(0)

