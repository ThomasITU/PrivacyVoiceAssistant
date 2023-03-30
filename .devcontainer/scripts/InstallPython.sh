#!/usr/bin/env bash

apt update && apt upgrade -y
apt install wget build-essential libncursesw5-dev libssl-dev -y\
     libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev -y

# download and install python 3.10.8

directory=/privacyVoiceAssistant/lib/Python-3.10.8 
if [ -d "$directory" ]; then
    echo "$directory exists."
else 
    wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz -O /privacyVoiceAssistant/lib//Python-3.10.8.tgz
    cd /privacyVoiceAssistant/lib/
    tar xzf Python-3.10.8.tgz 
    rm Python-3.10.8.tgz
    cd Python-3.10.8 
    ./configure --enable-optimizations 
    make altinstall 
    cd /../privacyVoiceAssistant/
fi

pip3.10 install --upgrade pip
pip3.10 install speechbrain
pip3.10 install jsonpickle
pip3.10 install ipython

pip3.10 install -r requirements.txt