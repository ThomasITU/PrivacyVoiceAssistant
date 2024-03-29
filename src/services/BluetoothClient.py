#!/usr/bin/env python3
import sys
from os import getcwd
import copy as _
import bluetooth
from bluetooth import *

sys.path.append(getcwd() + "/../")
from util.Generate import Generate as _
from util.SaveAndLoad import SaveAndLoad
from model.Profile import Profile


def printNearbyDevices():
    devices = discover_devices(duration=15)
    for device in devices:
        print(device)

def connectToNearbyDevice(name="VoiceAssistant", uuid="94f39d29-7d6d-437d-973b-fba39e49d4ee", targetMacAddress=None) -> bluetooth.BluetoothSocket:
    try:
        if len(targetMacAddress) == 0:
            service_matches = bluetooth.find_service(name=name, uuid=uuid)
        else:
            service_matches = bluetooth.find_service(address=targetMacAddress)
        if len(service_matches) == 0:
            print(f"Couldn't find the service {name}, {uuid} with address: {targetMacAddress}")
            return None
        
        first_match = service_matches[0]
        port:int = first_match["port"]
        # adjust according to server
        port = 1 
        targetMacAddress = first_match["host"]
        return connectToDevice(port, name, targetMacAddress)
    except OSError as e:
        print(e)

def connectToDevice(port:int, name:str, targetMacAddress) -> bluetooth.BluetoothSocket:
    print("Connecting to \"{}\" on {}".format(name, targetMacAddress))
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((targetMacAddress, port))
    print("Connected")
    return sock

def sendProfile(sock:BluetoothSocket, profile = _.dummyProfile()):
    while "y" in input("Send profile? (y/n): ").lower():
        if isinstance(profile, Profile) == True:
            encoded = SaveAndLoad.encode(profile)
            sock.send(encoded)
    sock.close()

def main():
    while "y" in input("Print nearby devices? (y/n): ").lower():
        printNearbyDevices()
    
    targetMacAddress = input("Enter the address of the device you want to connect to (leave blank if unsure): ")
    sock = connectToNearbyDevice(targetMacAddress=targetMacAddress)
    sendProfile(sock)
    print("Done")


if __name__ == "__main__":
    main()