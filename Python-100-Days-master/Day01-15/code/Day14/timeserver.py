from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    # 1. Create a socket object and specify which transport service to use
    # family=AF_INET - IPv4 address
    # family=AF_INET6 - IPv6 address
    # type=SOCK_STREAM - TCP socket
    # type=SOCK_DGRAM - UDP socket
    # type=SOCK_RAW - raw socket
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2. Bind IP address and port (distinguish different services)
    server.bind(('192.168.1.2', 6789))
    # 3. Enable listening - listen for client connections to the server
    server.listen(512)
    print('The server starts and starts listening...')
    # 4. Receive the client's connection through the loop and make corresponding processing (provide service)
    while True:
        # accept method is a blocking method if no client is connected to the server
        # This method will block the code and will not execute down
        # The accept method returns a tuple where the first element is the client object
        # The second element is the address of the client (consisting of IP and port)
        client, addr = server.accept()
        print(str(addr) + 'Connected to the server.')
        # 5. Send data
        client.send(str(datetime.now()).encode('utf-8'))
        # 6. Disconnect
        client.close()


if __name__ == '__main__':
    main()