import colorama
import os


def clear():
    os.system('clear')


def main_menu():
    print()
    print(fr'''{colorama.Fore.GREEN}
                             _________                                      
              _____   ____  /   _____/ ______________  __ ___________       
             /     \_/ ___\ \_____  \_/ __ \_  __ \  \/ // __ \_  __ \      
            |  Y Y  \  \___ /        \  ___/|  | \/\   /\  ___/|  | \/      
            |__|_|  /\___  >_______  /\___  >__|    \_/  \___  >__|         
                  \/     \/        \/     \/                 \/ {colorama.Style.RESET_ALL}          
         
          1 - My servers
          2 - Create server  
          3 - Delete server  
          4 - Settings  
          5 - Check version   
          0 - Exit''' + '\n'*6)
    return 


def settings_menu():
    print(fr'''{colorama.Fore.GREEN}
            _________       __    __  .__
           /   _____/ _____/  |__/  |_|__| ____    ____  ______ 
           \_____  \_/ __ \   __\   __\  |/    \  / ___\/  ___/ 
           /        \  ___/|  |  |  | |  |   |  \/ /_/  >___ \
          /_______  /\___  >__|  |__| |__|___|  /\___  /____  >
                  \/     \/                   \//_____/     \/ 
    {colorama.Style.RESET_ALL}''')
    return 


def VersionMenu():
    print(fr'''{colorama.Fore.GREEN} 
    ____   ____                  .__                      
    \   \ /   /___________  _____|__| ____   ____   ______
     \   Y   // __ \_  __ \/  ___/  |/  _ \ /    \ /  ___/
      \     /\  ___/|  | \/\___ \|  (  <_> )   |  \\___ \ 
       \___/  \___  >__|  /____  >__|\____/|___|  /____  >
                  \/           \/               \/     \/
    {colorama.Style.RESET_ALL}''')
    return


if __name__ == '__main__':
    settings_menu()
    main_menu()
    VersionMenu()

