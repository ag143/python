"""
Using Multithreading - Simulate Multiple Download Tasks

Version: 0.1
Author: author
Date: 2018-03-20
"""

from random import randint
from threading import Thread
from time import time, sleep


def download_task(filename):
     print('Start downloading %s...' % filename)
     time_to_download = randint(5, 10)
     sleep(time_to_download)
     print('%s download completed! It took %d seconds' % (filename, time_to_download))


def main():
     start = time()
     thread1 = Thread(target=download_task, args=('Python from entry to hospital.pdf',))
     thread1.start()
     thread2 = Thread(target=download_task, args=('Peking Hot.avi',))
     thread2.start()
     thread1.join()
     thread2.join()
     end = time()
     print('It took %.3f seconds in total' % (end - start))


if __name__ == '__main__':
     main()