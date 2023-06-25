import bluetooth
from bluetooth import *

def receiveMessages():
  server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  
  port = 1
  server_sock.bind(("",port))
  server_sock.listen(1)
  
  client_sock,address = server_sock.accept()
  print("Accepted connection from " + str(address))
  
  data = client_sock.recv(1024)
  print("received [%s]" % data)
  
  client_sock.close()
  server_sock.close()
  
def sendMessageTo(targetBluetoothMacAddress):
  port = 1
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send("Message Recieved")
  sock.close()
  
def lookUpNearbyBluetoothDevices():
  my_phone = 'Pixel 6'
  my_address = None

  nearby_devices = bluetooth.discover_devices()
  for bdaddr in nearby_devices:
    if my_phone == str(bluetooth.lookup_name( bdaddr )):
      print()
      my_address = bdaddr

      sendMessageTo(my_address)
    
    
my_phone = 'Pixel 6'
my_address = None

nearby_devices = bluetooth.discover_devices()
for bdaddr in nearby_devices:
  if my_phone == str(bluetooth.lookup_name( bdaddr )):
    print(my_address)
    my_address = bdaddr

    port = [_ for _ in find_service(address=bt_addr) if 'RFCOMM' in _['protocol']][0]['port']
    s = BluetoothSocket(RFCOMM)
    s.connect((bt_addr, port))