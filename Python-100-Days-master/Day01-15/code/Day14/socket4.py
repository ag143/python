"""
Sockets - Create an Echo client based on the UDP protocol

Version: 0.1
Author: Luo Hao
Date: 2018-03-22
"""

from socket import *

client = socket(AF_INET, SOCK_DGRAM)
while True:
     data_str = input('Please input: ')
     client.sendto(data_str.encode('utf-8'), ('localhost', 6789))
     data, addr = client.recvfrom(1024)
     data_str = data.decode('utf-8')
     print('Server response:', data_str)
     if data_str == 'bye':
         break
client.close()