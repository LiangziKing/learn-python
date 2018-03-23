#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-23 10:30:53
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-23 10:32:22

import functools

int2 = functools.partial(int, base=2)

print('1000000 = ', int2('1000000'))
print('1010101 = ', int2('1010101'))