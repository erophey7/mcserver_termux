import colorama
import os




colorama.init()


class ui():

    def clear():
        os.system("clear")

    def main_menu():
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
        print(f"\n\n\n\n\n")
        




ui.main_menu()

input()