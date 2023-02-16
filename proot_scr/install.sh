#!/bin/sh
apt update
apt -y upgrade
apt install -y git openjdk-8* openjdk-17*
mkdir /root/servers
exit