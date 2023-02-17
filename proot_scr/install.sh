#!/bin/sh
apt update && apt -y upgrade && apt install -y git openjdk-8-jdk openjdk-17-jdk && mkdir /root/servers
