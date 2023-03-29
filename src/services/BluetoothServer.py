#!/usr/bin/env python3
import sys
from os import getcwd
import copy as _
from uuid import uuid4
import socket
import bluetooth
from bluetooth import *

sys.path.append(getcwd() + "/../")
print(sys.path)

from model.Profile import Profile
from util.SaveAndLoad import SaveAndLoad


# Constants
BUFFER_SIZE = 1024
DEFAULT_PROFILE_PATH = "/PivacyVoiceAssistant/resources/profiles/"


def createServer(uuid="94f39d29-7d6d-437d-973b-fba39e49d4ee", name="VoiceAssistant") -> tuple[int, bluetooth.BluetoothSocket]:
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    hostMACAddress = getBluetoothAddress("none")
    port = bluetooth.PORT_ANY
    print(hostMACAddress)
    print(port)
    server_sock.bind((hostMACAddress, port))
    

    server_sock.listen(1)

    bluetooth.advertise_service(server_sock, name, service_id=uuid,
                service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                profiles=[bluetooth.SERIAL_PORT_PROFILE],
                protocols=[bluetooth.OBEX_UUID]
                )
    port = server_sock.getsockname()[1]
    print(f"UUID: {uuid} - Listening on port {port}...")
    return port, server_sock

def getBluetoothAddress(mode:str) -> str:
    if mode == "hci":
        cmd = "hciconfig"
        device_id = "hci1" 
        stream = os.popen(cmd)
        output = stream.read()
        bt_mac = output.split("{}:".format(device_id))[1].split("BD Address: ")[1].split(" ")[0].strip()
        return bt_mac
    return bluetooth.read_local_bdaddr()[0]

def acceptConnections(server_sock:bluetooth.BluetoothSocket, port:int):
    try:
        while True:
            print("Waiting for connection on RFCOMM channel", port)

            client_sock, client_info = server_sock.accept()
            print("Accepted connection from", client_info)
            data = client_sock.recv(BUFFER_SIZE)
            if not data:
                break
            profile:Profile = SaveAndLoad.decode(data)

            path = getcwd() + "/../../resources/profiles/"
            profileReceived(profile, path)
            
            client_sock.close()
            print("Disconnected.")
    except OSError:
        print("Bluetooth connection closed unexpectly.")
    server_sock.close()

def profileReceived(profile:Profile, path = DEFAULT_PROFILE_PATH):
    if profile is None or isinstance(profile,Profile) == False:
        return
    print(f"Received profile: {profile}")
    path += str(hash(profile)) + ".json"
    SaveAndLoad.saveAsJson(path, profile)
    if(os.path.isfile(path)):
        print(f"Saved profile to {path}")
    else:
        print(f"Failed to save profile to {path}")
        raise Exception(f"Failed to save profile at {path}")

def main():
    port, server_sock = createServer()
    acceptConnections(server_sock, port)
    print("All done.")

if __name__ == '__main__':
    main()