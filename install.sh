#!/data/data/com.termux/files/usr/bin/sh
termux-setup-storage
apt update && apt upgrade -y
apt install -y python busybox openjdk-17 wget net-tools termux-services proot resolv-conf openssl-tool screen proot-distro toilet
pip install -r requirements.txt

if test -d "$PREFIX/var/lib/proot-distro/installed-rootfs/ubuntu";
then
        echo ""
else
        proot-distro clear-cache
        proot-distro install ubuntu
fi

ngrok
screen -dmS mcserver_install
screen -S mcserver_install -X stuff "proot-distro login ubuntu --bind "${PWD}"/proot_scr:/root; exit\n"
screen -S mcserver_install -X stuff "chmod 777 install.sh && ./install.sh; exit\n"
screen -r mcserver_install
rm -rf ${PREFIX}/bin/mcserver
export EXECCOMMAND='cd '${PWD}' && python main.py'
echo ${EXECCOMMAND} > ${PREFIX}/bin/mcserver
chmod +x ${PREFIX}/bin/mcserver
clear && printf "\033[0;32m$(toilet "install")\n\033[1;32m $(toilet "complete")\n\n\033[0;32mTo run use mcserver\n"
