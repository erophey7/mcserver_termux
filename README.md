# mcserver_termux
Инструмент для создания сервера Java Minecraft в Termux с открытым исходным кодом.

 

Установка:

    apt update && apt upgrade -y
    apt install -y git
    git clone https://github.com/erophey7/mcserver_termux.git
    cd mcserver-termux
    chmod +x install.sh
    ./install.sh

Использование:

    mcserver

после установки неообходимо задать ngrok authtoken, получить его можно получить после регистрации не сайте
https://dashboard.ngrok.com/get-started/your-authtoken.

далее выполняем

    mcserver

и идём в настройки, там выбираем параметр Ngrok authtoken написав 7, после вставляя полученный токен.



