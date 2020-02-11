#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import aiohttp
import asyncio
from datetime import datetime


async def aio_2():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.geekdigging.com/') as resp:
            print(resp.status)
            print(await resp.text())

loop = asyncio.get_event_loop()
loop.run_until_complete(aio_2())


async def aio_3():
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout = timeout) as session:
        async with session.get('https://www.geekdigging.com/', timeout = timeout) as resp:
            print(resp.status)

loop = asyncio.get_event_loop()
loop.run_until_complete(aio_3())