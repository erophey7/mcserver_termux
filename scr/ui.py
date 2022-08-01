import colorama
import os


def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
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
0 - Exit''' + '\n'*3)
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

def Core_menu():
    print(fr'''{colorama.Fore.GREEN} 
 _________                       
 \_   ___ \  ___________   ____  
 /    \  \/ /  _ \_  __ \_/ __ \ 
 \     \___(  <_> )  | \/\  ___/ 
  \______  /\____/|__|    \___  >
         \/                   \/ 
    {colorama.Style.RESET_ALL}
    Select server core 
    
1 - Vanila core
2 - Forge
3 - Spigot''' + '\n'*6)
    return

def server_name():
    print(fr'''{colorama.Fore.GREEN} 
 _______                         
 \      \ _____    _____   ____  
 /   |   \\__  \  /     \_/ __ \ 
/    |    \/ __ \|  Y Y  \  ___/ 
\____|__  (____  /__|_|  /\___  >
        \/     \/      \/     \/ 
    {colorama.Style.RESET_ALL}
    Type server name (a-Z 0-9 _ -) 

''' + '\n' * 6)
    return

if __name__ == '__main__':
    settings_menu()
    main_menu()
    VersionMenu()
