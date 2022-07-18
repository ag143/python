"""
Implement inter-process communication

Version: 0.1
Author: author
Date: 2018-03-20
"""
import multiprocessing
import os


def sub_task(queue):
     print('Subprocess process number:', os.getpid())
     counter = 0
     while counter < 1000:
         queue.put('Pong')
         counter += 1


if __name__ == '__main__':
     print('Current process ID:', os.getpid())
     queue = multiprocessing.Queue()
     p = multiprocessing.Process(target=sub_task, args=(queue,))
     p.start()
     counter = 0
     while counter < 1000:
         queue.put('Ping')
         counter += 1
     p.join()
     print('The subtask has been completed.')
     for_in range(2000):
         print(queue.get(), end='')