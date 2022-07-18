"""
socket - create a time server based on the TCP protocol

Version: 0.1
Author: Luo Hao
Date: 2018-03-22
"""

from socket import *
from time import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 6789))
server.listen()
print('The server has been started and is listening for client connections.')
while True:
     client, addr = server.accept()
     print('Client %s:%d successfully connected.' % (addr[0], addr[1]))
     currtime = localtime(time())
     timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
     client.send(timestr.encode('utf-8'))
     client.close()
server.close()