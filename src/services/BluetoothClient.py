#!/usr/bin/env python3
"""PyBluez simple example rfcomm-client.py

Simple demonstration of a client application that uses RFCOMM sockets intended
for use with rfcomm-server.

Author: Albert Huang <albert@csail.mit.edu>
$Id: rfcomm-client.py 424 2006-08-24 03:35:54Z albert $
"""
import sys
from os import getcwd
import copy as _
sys.path.append(getcwd() + "/../")

import bluetooth
from bluetooth import *
from util.Generate import Generate as _
from util.SaveAndLoad import SaveAndLoad

profile = _.dummyProfile()
encoded = SaveAndLoad.encode(profile)
print(encoded)
print(profile)

def lookUpNearbyBluetoothDevices(): 
  devices = discover_devices(duration=15, lookup_names=True)
  for device in devices:
    print(device)
  for device in devices:
    print([_ for _ in find_service(address=device) if 'RFCOMM' in _['protocol'] ])
    # now manually select the desired device or hardcode its name/mac whatever in the script


lookUpNearbyBluetoothDevices()
addr = input("Enter the address of the device you want to connect to: ")

# search for the SampleServer service
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
service_matches = bluetooth.find_service(name="SampleServer",uuid=uuid, address=addr)

if len(service_matches) == 0:
    print("Couldn't find the SampleServer service.")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"{}\" on {}".format(name, host))

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

print("Connected. Type something...")
while True:
    sock.send(encoded)
    data = input()
    if not data:
        break

sock.close()