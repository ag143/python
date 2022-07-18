"""
Encrypt and decrypt
Symmetric encryption - encryption and decryption are the same key - DES/AES
Asymmetric encryption - encryption and decryption are different keys - RSA
pip install pycrypto
"""
import base64

from hashlib import md5

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA

# # AES encryption key (length 32 bytes)
# key = md5(b'1qaz2wsx').hexdigest()
# # AES encrypted initial vector (randomly generated)
# iv = Random.new().read(AES.block_size)


def main():
    """Main function"""
    # Generate key pair
    key_pair = RSA.generate(1024)
    # import public key
    pub_key = RSA.importKey(key_pair.publickey().exportKey())
    # import private key
    pri_key = RSA.importKey(key_pair.exportKey())
    message1 = 'hello, world!'
    # encrypt data
    data = pub_key.encrypt(message1.encode(), None)
    # BASE64 encode encrypted data
    message2 = base64.b64encode(data[0])
    print(message2)
    # BASE64 decode the encrypted data
    data = base64.b64decode(message2)
    # decrypt data
    message3 = pri_key.decrypt(data)
    print(message3.decode())
    # # AES - Symmetric encryption
    # str1 = 'I love you all! '
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # # Encrypt
    # str2 = cipher.encrypt(str1)
    # print(str2)
    ## decrypt
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # str3 = cipher.decrypt(str2)
    # print(str3.decode())


if __name__ == '__main__':
    main()