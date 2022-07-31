import colorama
import os

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


def settings_menu():
    print("")
    print(colorama.Fore.GREEN + "   _________       __    __  .__                       \n",
          "  /   _____/ _____/  |__/  |_|__| ____    ____  ______ \n"
          "  \_____  \_/ __ \   __\   __\  |/    \  / ___\/  ___/ \n",
          "  /        \  ___/|  |  |  | |  |   |  \/ /_/  >___ \  \n",
          " /_______  /\___  >__|  |__| |__|___|  /\___  /____  > \n",
          "         \/     \/                   \//_____/     \/  \n")
    print(colorama.Style.RESET_ALL)
