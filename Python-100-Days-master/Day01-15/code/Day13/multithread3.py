"""
Using Multithreading - Simulate Multiple Download Tasks

Version: 0.1
Author: author
Date: 2018-03-20
"""

from random import randint
from time import time, sleep
import threading


class DownloadTask(threading.Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('Start downloading %s...' % self._filename)
        time_to_download = randint(5, 10)
        print('Remaining time %d seconds.' % time_to_download)
        sleep(time_to_download)
        print('%s download complete!' % self._filename)


def main():
    start = time()
    # Put multiple download tasks into multiple threads for execution
    # Create a thread object through a custom thread class. After the thread starts, it will call back and execute the run method
    thread1 = DownloadTask('Python from entry to hospital.pdf')
    thread1.start()
    thread2 = DownloadTask('Peking Hot.avi')
    thread2.start()
    thread1.join()
    thread2.join()
    end = time()
    print('It took %.3f seconds in total' % (end - start))


if __name__ == '__main__':
    main()

# Please note that threads created by threading.Thread are non-daemon threads by default