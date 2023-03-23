#!/usr/bin/env bash
apt-get install libbluetooth-dev -y
apt-get install bluez -y
apt-get install dbus -y

pip3.10 install --upgrade pip setuptools==57.5.0
pip3.10 install git+https://github.com/pybluez/pybluez.git#egg=pybluez

mkdir /var/run/sdp

service dbus start
service bluetooth start
hciconfig hci0 down
hciconfig hci0 up
sdptool add SP
hciconfig hci0 piscan