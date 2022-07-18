"""
Using Multithreading - Simulate Multiple Download Tasks

Version: 0.1
Author: author
Date: 2018-03-20
"""

from random import randint
from time import time, sleep
import atexit
import _thread


def download_task(filename):
    print('Start downloading %s...' % filename)
    time_to_download = randint(5, 10)
    print('Remaining time %d seconds.' % time_to_download)
    sleep(time_to_download)
    print('%s download complete!' % filename)


def shutdown_hook(start):
    end = time()
    print('It took %.3f seconds in total.' % (end - start))


def main():
    start = time()
    # Put multiple download tasks into multiple threads for execution
    thread1 = _thread.start_new_thread(download_task, ('Python from entry to hospital.pdf',))
    thread2 = _thread.start_new_thread(download_task, ('Peking Hot.avi',))
    # Register the shutdown hook to calculate the execution time before the program execution ends
    atexit.register(shutdown_hook, start)


if __name__ == '__main__':
    main()

# Executing the code here will cause a fatal error (don't be scared by the word) because the download thread will have problems if it tries to execute it after the main thread ends
# Need to explain because the _thread module is a relatively low-level thread operation and does not support the concept of daemon threads
# There will be a lot of inconvenience in actual development, so we recommend using the advanced operations provided by the threading module for multi-threaded programming