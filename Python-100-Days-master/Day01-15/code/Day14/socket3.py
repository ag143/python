"""
Socket - Echo server based on UDP protocol

Version: 0.1
Author: Luo Hao
Date: 2018-03-22
"""
from socket import *
from time import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('localhost', 6789))
while True:
     data, addr = server.recvfrom(1024)
     server.sendto(data, addr)
server.close()