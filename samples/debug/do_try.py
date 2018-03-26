#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-26 11:29:28
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-26 11:31:13

try:
	print('try...')
	r = 10 / 0
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally...')
print('END')