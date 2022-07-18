"""
aiohttp - Asynchronous HTTP network access
Asynchronous I/O (asynchronous programming) - using only one thread (single thread) to handle user requests
Once the user request is accepted, the rest are all I/O operations, and the effect of concurrency can also be achieved by multiplexing I/O.
This approach results in higher CPU utilization compared to multithreading because there is no thread switching overhead
Redis/Node.js - Single Thread + Asynchronous I/O
Celery - Asynchronous processing of time-consuming tasks to be executed
Asynchronous I/O Event Loop - uvloop
"""
import asyncio
import re

import aiohttp


async def fetch(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def main():
    pattern = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    async with aiohttp.ClientSession() as session:
        for url in urls:
            html = await fetch(session, url)
            print(pattern.search(html).group('title'))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()