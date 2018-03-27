#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-27 15:18:36
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-27 15:19:21

from contextlib import contextmanager

@contextmanager
def closing(fname):
    f = None
    try:
        f = open(fname, 'r')
        yield f
    finally:
        if f:
            f.close()

with closing('test.txt') as f:
    print(f.read())
