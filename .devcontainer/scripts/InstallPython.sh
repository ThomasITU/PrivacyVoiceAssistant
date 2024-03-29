#!/usr/bin/env bash

apt update && apt upgrade -y
apt install wget build-essential libncursesw5-dev libssl-dev -y\
     libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev -y

# download and install python 3.10.8

directory=/privacyVoiceAssistant/lib/Python-3.10.8.tgz 
if ! [ -d "$directory" ]; then
    echo "$directory does not exists."
    wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz -O /privacyVoiceAssistant/lib//Python-3.10.8.tgz    
fi

echo "installing python 3.10.8"

cd /privacyVoiceAssistant/lib/
tar xzf Python-3.10.8.tgz 
cd Python-3.10.8 
./configure --enable-optimizations 
make altinstall 
cd /../privacyVoiceAssistant/


python3.10 -m pip install speechbrain
python3.10 -m pip install jsonpickle
python3.10 -m pip install ipython
pip install --upgrade pip

python3.10 -m pip install -r requirements.txt