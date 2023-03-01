# Uses Bluez for Linux
#
# sudo apt-get install bluez python-bluez
# 
# Taken from: https://people.csail.mit.edu/albert/bluez-intro/x232.html
# Taken from: https://people.csail.mit.edu/albert/bluez-intro/c212.html

import bluetooth

from bluetooth import  *

def receiveMessages():
  server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  
  port = 1
  server_sock.bind(("",port))
  server_sock.listen(1)
  
  client_sock, address = server_sock.accept()
  print ("Accepted connection from " + str(address))
  
  data = client_sock.recv(1024)
  print ("received [%s]" % data)
  
  client_sock.close()
  server_sock.close()
  
def sendMessageTo(targetBluetoothMacAddress):
  targetPort = [_ for _ in find_service(address=targetBluetoothMacAddress) if 'RFCOMM' in _['protocol']][0]['port']
  print (targetPort)
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, targetPort))
  sock.send("hello!!")
  sock.close()
  
def lookUpNearbyBluetoothDevices(): 
  devices = discover_devices()
  for device in devices:
    print([_ for _ in find_service(address=device) if 'RFCOMM' in _['protocol'] ])
    # now manually select the desired device or hardcode its name/mac whatever in the script

    
lookUpNearbyBluetoothDevices()

i = 0
while i < 3:
  i += 1
  bt_addr = input("Enter macAddress: \n")
  sendMessageTo(bt_addr)
