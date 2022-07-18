"""
Create multiple processes using the Process class

Version: 0.1
Author: author
Date: 2018-03-20
"""

# Through the execution results of the following program, it can be confirmed that the parent process copied the process and its data structure when creating the child process
# Each process has its own independent memory space, so sharing data between processes can only be done through IPC


from multiprocessing import Process, Queue, current_process
from time import sleep


def sub_task(content, counts):
     print(f'PID: {current_process().pid}')
     counter = 0
     while counter < counts:
         counter += 1
         print(f'{counter}: {content}')
         sleep(0.01)


def main():
     number = random.randrange(5, 10)
     Process(target=sub_task, args=('Ping', number)).start()
     Process(target=sub_task, args=('Pong', number)).start()


if __name__ == '__main__':
     main()