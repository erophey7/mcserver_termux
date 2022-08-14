termux-setup-storage
apt update && apt upgrade -y
apt install -y python busybox openjdk-17 wget net-tools termux-services proot resolv-conf openssl-tools
pip install -r requirements.txt
ngrok