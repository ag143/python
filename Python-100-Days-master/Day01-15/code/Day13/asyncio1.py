"""
Asynchronous I/O operations - asyncio module

Version: 0.1
Author: author
Date: 2018-03-21
"""

import asyncio
import threading
# import time


@asyncio.coroutine
def hello():
     print('%s: hello, world!' % threading.current_thread())
     # Sleep does not block the main thread because it uses asynchronous I/O operations
     # Note that there is a yield from to wait for the hibernation operation to complete
     yield from asyncio.sleep(2)
     # asyncio.sleep(1)
     # time.sleep(1)
     print('%s: goodbye, world!' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# Wait for two asynchronous I/O operations to complete
loop.run_until_complete(asyncio.wait(tasks))
print('game over!')
loop.close()