apt update && apt upgrade -y
apt install -y python busybox openjdk-17 wget net-tools termux-services
pip install -r requirements.txt
termux-setup-storage
