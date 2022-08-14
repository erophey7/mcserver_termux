termux-setup-storage
apt update && apt upgrade -y
apt install -y python busybox openjdk-17 wget net-tools termux-services proot resolv-conf openssl-tools
pip install -r requirements.txt
ngrok
rm -rf ${PREFIX}/bin/mcserver
chmod +x start.sh
ln -sf ${PWD}/start.sh ${PREFIX}/bin/mcserver
chmod +x ${PREFIX}/bin/mcserver