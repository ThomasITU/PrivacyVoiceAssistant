#!/usr/bin/env bash

# create a directory for apt to store its cache
path="/var/cache/apt"
mkdir $path
mkdir $path/amd64
mkdir $path/amd64/archives
mkdir $path/amd64/archives/partial
apt install vim -y

echo "installing python"
source /privacyVoiceAssistant/scripts/InstallPython.sh

echo "setting up bluetooth"
source /privacyVoiceAssistant/scripts/SetupBluetooth.sh