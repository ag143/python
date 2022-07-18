from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():

    # custom thread class
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON is plain text and cannot carry binary data
            # So the binary data of the picture should be processed into base64 encoding
            my_dict['filedata'] = data
            # Process the dictionary into a JSON string through the dumps function
            json_str = dumps(my_dict)
            # Send JSON string
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1. Create a socket object and specify which transport service to use
    server = socket()
    # 2. Bind IP address and port (distinguish different services)
    server.bind(('192.168.1.2', 5566))
    # 3. Enable listening - listen for client connections to the server
    server.listen(512)
    print('The server starts and starts listening...')
    with open('guido.jpg', 'rb') as f:
        # Process the binary data into base64 and decode it into a string
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # Use a dictionary (key-value pair) to store various data to be sent
        # Later, the dictionary can be processed into JSON format and passed on the network
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()