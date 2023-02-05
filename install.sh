termux-setup-storage
apt update && apt upgrade -y
apt install -y python busybox openjdk-17 wget net-tools termux-services proot resolv-conf openssl-tool screen
pip install -r requirements.txt
ngrok
rm -rf ${PREFIX}/bin/mcserver
export EXECCOMMAND='cd '${PWD}' && python main.py'
echo ${EXECCOMMAND} > ${PREFIX}/bin/mcserver
chmod +x ${PREFIX}/bin/mcserver
