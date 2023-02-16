termux-setup-storage
apt update && apt upgrade -y
apt install -y python busybox openjdk-17 wget net-tools termux-services proot resolv-conf openssl-tool screen proot-distro
pip install -r requirements.txt
proot-distro install ubuntu
ngrok
screen -dmS mcserver_install
screen -S mcserver_install -X stuff "proot-distro login ubuntu --bind "${PWD}"/proot_scr:/root\n"
screen -S mcserver_install -X stuff "chmod 777 install.sh && ./install.sh"
screen -S mcserver_install -X stuff "exit\n"
screen -r mcserver_install
rm -rf ${PREFIX}/bin/mcserver
export EXECCOMMAND='cd '${PWD}' && python main.py'
echo ${EXECCOMMAND} > ${PREFIX}/bin/mcserver
chmod +x ${PREFIX}/bin/mcserver
