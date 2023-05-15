#!/usr/bin/env sh

# create a directory for apt to store its cache

path="/var/cache/apt"
mkdir $path
mkdir $path/amd64
mkdir $path/amd64/archives
mkdir $path/amd64/archives/partial
apt install vim -y

if [ -d "$path" ]; then
    echo "$path exists."
else 
  echo "$path does not exist."
fi

mkdir /tmp/voiceModels
mkdir /tmp/voiceFiles
mkdir /tmp/intents
