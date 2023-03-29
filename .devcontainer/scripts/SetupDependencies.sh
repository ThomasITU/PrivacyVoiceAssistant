#!/usr/bin/env bash

# create a directory for apt to store its cache

path="/var/cache/apt"
if [ -d "$directory" ]; then
    echo "$directory exists."
else 
    wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz -O /tmp/Python-3.10.8.tgz
    cd /tmp/
    tar xzf Python-3.10.8.tgz 
    rm Python-3.10.8.tgz
    cd Python-3.10.8 
    ./configure --enable-optimizations 
    make altinstall 
    cd ../../privacyVoiceAssistant/src/
fi
mkdir $path
mkdir $path/amd64
mkdir $path/amd64/archives
mkdir $path/amd64/archives/partial
apt install vim -y

echo "installing python"
source /privacyVoiceAssistant/scripts/InstallPython.sh

# echo "setting up bluetooth"
# source /privacyVoiceAssistant/scripts/SetupBluetooth.sh