#!/usr/bin/env bash
path ="/var/cache/apt"

mkdir $path/amd64
mkdir $path/amd64/archives
mkdir $path/amd64/archives/partial
apt-get update && apt-get install -y vim