#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-27 15:01:32
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-27 15:10:16

import threading
import asyncio

async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
