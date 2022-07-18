from socket import socket
from json import loads
from base64 import b64decode


def main():
     client = socket()
     client.connect(('192.168.1.2', 5566))
     # define an object that holds binary data
     in_data = bytes()
     # Since I don't know how big the data sent by the server is, it receives 1024 bytes each time
     data = client.recv(1024)
     while data:
         # Concatenate the received data
         in_data += data
         data = client.recv(1024)
     # Decode the received binary data into a JSON string and convert it to a dictionary
     # The role of the loads function is to convert the JSON string into a dictionary object
     my_dict = loads(in_data.decode('utf-8'))
     filename = my_dict['filename']
     filedata = my_dict['filedata'].encode('utf-8')
     with open('/Users/Hao/' + filename, 'wb') as f:
         # Decode data in base64 format into binary data and write to file
         f.write(b64decode(filedata))
     print('The picture has been saved.')


if __name__ == '__main__':
     main()