"""
Encoding and Decoding - BASE64
0-9A-Za-z+/
1100 0101 1001 0011 0111 0110
00110001 00011001 00001101 00110110
base64
b64encode / b64decode
-------------------------------------
Serialize and deserialize
Serialize - turn an object into a sequence of bytes (bytes) or a sequence of characters (str) - serialize / pickle
Deserialization - restore a sequence of bytes or characters to an object
Python standard library support for serialization:
json - serialization in character form
pickle - Serialization in bytes
dumps / loads
"""
import base64
import json
import redis

from example02 import Person


class PersonJsonEncoder(json.JSONEncoder):

    def default(self, o):
        return o.__dict__


def main():
    cli = redis.StrictRedis(host='120.77.222.217', port=6379,
                            password='123123')
    data = base64.b64decode(cli.get('guido'))
    with open('guido2.jpg', 'wb') as file_stream:
        file_stream.write(data)
    # with open('guido.jpg', 'rb') as file_stream:
    # result = base64.b64encode(file_stream.read())
    # cli.set('guido', result)
    # persons = [
    # Person('Luo Hao', 39), Person('The King's Hammer', 18),
    # Person('Bai Yuanfang', 25), Person('Di Renjie', 37)
    # ]
    # persons = json.loads(cli.get('persons'))
    # print(persons)
    # cli.set('persons', json.dumps(persons, cls=PersonJsonEncoder))


if __name__ == '__main__':
    main()