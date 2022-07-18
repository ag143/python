"""
Scalable system performance
- Vertical scaling - increasing single node processing power
- Horizontal scaling - Turn a single node into a multi-node (read-write split/distributed cluster)
Concurrent Programming - Accelerates Program Execution / Improves User Experience
Time-consuming tasks are executed as independently as possible without blocking other parts of the code
- Multithreading
1. Create a Thread object specifying target and args properties and start the thread through the start method
2. Inherit the Thread class and override the run method to define the tasks performed by the thread
3. Create a thread pool object ThreadPoolExecutor and submit the tasks to be executed through submit
The third way can obtain the execution result of the thread in the future through the result method of the Future object
You can also use the done method to determine whether the thread has finished executing
- multi-Progress
- Asynchronous I/O
"""
import glob
import os
import time

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from PIL import Image


# class ThumbnailThread(Thread):

# def __init__(self, infile):
# self.infile = infile
# super().__init__()

# def run(self):
# file, ext = os.path.splitext(self.infile)
# filename = file[file.rfind('/') + 1:]
# for size in (32, 64, 128):
# outfile = f'thumbnails/{filename}_{size}_{size}.png'
# image = Image.open(self.infile)
# image.thumbnail((size, size))
# image.save(outfile, format='PNG')


def gen_thumbnail(infile):
    file, ext = os.path.splitext(infile)
    filename = file[file.rfind('/') + 1:]
    for size in (32, 64, 128):
        outfile = f'thumbnails/{filename}_{size}_{size}.png'
        image = Image.open(infile)
        image.thumbnail((size, size))
        image.save(outfile, format='PNG')


# def main():
# start = time.time()
# threads = []
# for infile in glob.glob('images/*'):
# # t = Thread(target=gen_thumbnail, args=(infile, ))
# t = ThumbnailThread(infile)
# t.start()
# threads.append(t)
# for t in threads:
# t.join()
# end = time.time()
# print(f'Time: {end - start} seconds')


def main():
    pool = ThreadPoolExecutor(max_workers=30)
    futures = []
    start = time.time()
    for infile in glob.glob('images/*'):
        # submit method is a non-blocking method
        # Even if the number of worker threads has been exhausted, the submit method will accept the submitted task
        future = pool.submit(gen_thumbnail, infile)
        futures.append(future)
    for future in futures:
        # result method is a blocking method if the thread has not finished
        # The execution result of the thread cannot be obtained temporarily, and the code will block here
        future.result()
    end = time.time()
    print(f'Time: {end - start} seconds')
    # shutdown is also a non-blocking method, but if the submitted task has not been executed
    # The thread pool will not stop working and then submit the task after shutdown, it will not be executed and an exception will occur
    pool.shutdown()


if __name__ == '__main__':
    main()