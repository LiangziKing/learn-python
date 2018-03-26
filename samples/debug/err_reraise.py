#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-26 11:52:26
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-26 11:54:39

# err_reraise.py

def foo(s):
	n = int(s)
	if n==0:
		raise ValueError('invalid value: %s' % s)
	return 10 / 0

def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!')
		raise

bar()