"""
Without multithreading - simulate multiple download tasks

Version: 0.1
Author: author
Date: 2018-03-20
"""

from random import randint
from time import time, sleep


def download_task(filename):
     print('Start downloading %s...' % filename)
     time_to_download = randint(5, 10)
     sleep(time_to_download)
     print('Download completed! It took %d seconds' % time_to_download)


def main():
     start = time()
     download_task('Python from entry to hospitalization.pdf')
     download_task('Peking Hot.avi')
     end = time()
     print('It took %.2f seconds in total.' % (end - start))


if __name__ == '__main__':
     main()