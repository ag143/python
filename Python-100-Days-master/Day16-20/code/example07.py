"""
Hash digest - digital signature/fingerprint - one-way hash function (irreversible without inverse)
Application areas:
1. The user sensitive information in the database is saved as a hash digest
2. Generate a signature for the data to verify that the data has not been maliciously tampered with
3. The second transfer function of cloud storage service (duplication function)
"""


class StreamHasher():
    """Summary Generator"""

    def __init__(self, algorithm='md5', size=4096):
        """Initialization method
        @params:
            algorithm - Hash digest algorithm - TeX - LaTeX Stack Exchange
            size - the size of each read data
        """
        self.size = size
        cls = getattr(__import__('hashlib'), algorithm.lower())
        self.hasher = cls()
    

    def digest(self, file_stream):
        """Generate hexadecimal digest string"""
        # data = file_stream.read(self.size)
        # while data:
        # self.hasher.update(data)
        # data = file_stream.read(self.size)
        for data in iter(lambda: file_stream.read(self.size), b''):
            self.hasher.update(data)
        return self.hasher.hexdigest()

    def __call__(self, file_stream):
        return self.digest(file_stream)


def main():
    """Main function"""
    hasher1 = StreamHasher()
    hasher2 = StreamHasher('sha1')
    hasher3 = StreamHasher('sha256')
    with open('Python-3.7.2.tar.xz', 'rb') as file_stream:
        print(hasher1.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher2.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher3(file_stream))


if __name__ == '__main__':
    main()