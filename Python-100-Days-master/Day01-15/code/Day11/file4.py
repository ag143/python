"""
Read and write binary files

Version: 0.1
Author: author
Date: 2018-03-13
"""
import base64

with open('mm.jpg', 'rb') as f:
     data = f.read()
     # print(type(data))
     # print(data)
     print('Number of bytes:', len(data))
     # Process the image into BASE-64 encoding
     print(base64.b64encode(data))

with open('girl.jpg', 'wb') as f:
     f.write(data)
print('Writing completed!')