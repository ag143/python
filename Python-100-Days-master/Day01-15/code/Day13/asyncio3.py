"""
Asynchronous I/O operations - asyncio module

Version: 0.1
Author: author
Date: 2018-03-21
"""
import asyncio


async def wget(host):
     print('wget %s...' % host)
     connect = asyncio.open_connection(host, 80)
     # Asynchronously wait for the connection result
     reader, writer = await connect
     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' %host
     writer.write(header.encode('utf-8'))
     # Perform write operations in asynchronous I/O mode
     await writer.drain()
     while True:
         # Perform read operations in asynchronous I/O mode
         line = await reader.readline()
         if line == b'\r\n':
             break
         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
     writer.close()


loop = asyncio.get_event_loop()
# Create a list with three coroutines via generative syntax
hosts_list = ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
tasks = [wget(host) for host in hosts_list]
# The following method puts asynchronous I/O operations into EventLoop until execution is complete
loop.run_until_complete(asyncio.wait(tasks))
loop.close()