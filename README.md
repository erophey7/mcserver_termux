# mcserver_termux
Инструмент для создания Java Minecraft сервера в Termux с открытым исходным кодом.

 

Установка:

    apt update && apt upgrade -y
    apt install -y git
    git clone https://github.com/erophey7/mcserver_termux.git
    cd mcserver-termux
    chmod a+x install.sh
    ./install.sh

Использование:

    mcserver

после установки неообходимо задать ngrok authtoken, получить его можно получить после регистрации не сайте
https://dashboard.ngrok.com/get-started/your-authtoken.

далее запускаем утилиту, и идём в настройки, выбираем параметр Ngrok authtoken написав 7, после вставляем полученный токен.



