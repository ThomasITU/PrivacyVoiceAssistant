#!/usr/bin/env bash
apt-get install libbluetooth-dev -y
apt-get install git -y
apt-get install bluez -y

pip3.10 install --upgrade pip setuptools==57.5.0
pip3.10 install git+https://github.com/pybluez/pybluez.git#egg=pybluez


service dbus start
service bluetooth start
hciconfig hci0 piscan
sdptool add SP