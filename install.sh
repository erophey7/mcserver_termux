termux-setup-storage
apt update && apt upgrade -y
apt install -y python busybox openjdk-17 wget net-tools termux-services proot resolv-conf openssl-tools
pip install -r requirements.txt

echo "Downloading ngrok..."
case `dpkg --print-architecture` in
aarch64)
    architectureURL="arm64" ;;
arm)
    architectureURL="arm" ;;
armhf)
    architectureURL="arm" ;;
amd64)
    architectureURL="amd64" ;;
i*86)
    architectureURL="386" ;;
x86_64)
    architectureURL="amd64" ;;
*)
    echo "unknown or unsupported architecture"
esac

wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-${architectureURL}.zip -O ngrok.zip

unzip ngrok.zip
rm ngrok.zip