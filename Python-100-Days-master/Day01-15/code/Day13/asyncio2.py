"""
Asynchronous I/O operations - async and await

Version: 0.1
Author: author
Date: 2018-03-21
"""
import asyncio
import threading


# The function modified by async is no longer a normal function but a coroutine
# Note that async and await will appear as keywords in Python 3.7
async def hello():
     print('%s: hello, world!' % threading.current_thread())
     await asyncio.sleep(2)
     print('%s: goodbye, world!' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# Wait for two asynchronous I/O operations to complete
loop.run_until_complete(asyncio.wait(tasks))
loop.close()