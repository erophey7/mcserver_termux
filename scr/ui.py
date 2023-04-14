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
6 - Update Java   
0 - Exit''' + '\n'*2)
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
3 - Spigot
4 - Fabric
0 - Back''' + '\n'*4)
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
    Type server name (a-Z 0-9 -) 

''' + '\n' * 6)
    return

def my_servers():
    print(fr'''{colorama.Fore.GREEN} 
   _____                                                         
  /     \ ___.__.   ______ ______________  __ ___________  ______
 /  \ /  <   |  |  /  ___// __ \_  __ \  \/ // __ \_  __ \/  ___/
/    Y    \___  |  \___ \\  ___/|  | \/\   /\  ___/|  | \/\___ \ 
\____|__  / ____| /____  >\___  >__|    \_/  \___  >__|  /____  >
        \/\/           \/     \/                 \/           \/ 
    {colorama.Style.RESET_ALL}
''' + '\n' * 2)
    return

def Server_menu():
    print(fr'''{colorama.Fore.GREEN} 
  _________                                                              
 /   _____/ ______________  __ ___________    _____   ____   ____  __ __ 
 \_____  \_/ __ \_  __ \  \/ // __ \_  __ \  /     \_/ __ \ /    \|  |  \
 /        \  ___/|  | \/\   /\  ___/|  | \/ |  Y Y  \  ___/|   |  \  |  /
/_______  /\___  >__|    \_/  \___  >__|    |__|_|  /\___  >___|  /____/ 
        \/     \/                 \/              \/     \/     \/       
    {colorama.Style.RESET_ALL}
''' + '\n' * 2)
    return


def Delete_menu():
    print(fr'''{colorama.Fore.GREEN} 
________         .__          __          
\______ \   ____ |  |   _____/  |_  ____  
 |    |  \_/ __ \|  | _/ __ \   __\/ __ \ 
 |    `   \  ___/|  |_\  ___/|  | \  ___/ 
/_______  /\___  >____/\___  >__|  \___  >
        \/     \/          \/          \/ 
    {colorama.Style.RESET_ALL}
''' + '\n' * 2)
    return


def Properties_menu():
    print(fr'''{colorama.Fore.GREEN} 
__________                                     __  .__               
\______   \_______  ____ ______   ____________/  |_|__| ____   ______
 |     ___/\_  __ \/  _ \\____ \_/ __ \_  __ \   __\  |/ __ \ /  ___/
 |    |     |  | \(  <_> )  |_> >  ___/|  | \/|  | |  \  ___/ \___ \ 
 |____|     |__|   \____/|   __/ \___  >__|   |__| |__|\___  >____  >
                         |__|        \/                    \/     \/ 

    {colorama.Style.RESET_ALL}
''' + '\n' * 2)
    return




if __name__ == '__main__':
    settings_menu()
    main_menu()
    VersionMenu()

