# bluetooth notes

## ensure bluetooth software is up to date
sudo apt-get install libbluetooth-dev 


## bluetooth python library
pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez

pip install --upgrade pip setuptools==57.5.0

https://pybluez.readthedocs.io/en/latest/api/index.html


## bluetooth no advertisable device

sudo hciconfig hci0 piscan

## bluetooth server permission denied

https://stackoverflow.com/questions/34599703/rfcomm-bluetooth-permission-denied-error-raspberry-pi

## bluetooth server no such file or directory

https://stackoverflow.com/questions/36675931/bluetooth-btcommon-bluetootherror-2-no-such-file-or-directory