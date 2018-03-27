#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-27 15:17:51
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-27 15:19:01

from contextlib import contextmanager

@contextmanager
def log(name):
    print('[%s] start...' % name)
    yield
    print('[%s] end.' % name)

with log('DEBUG'):
    print('Hello, world!')
    print('Hello, Python!')
