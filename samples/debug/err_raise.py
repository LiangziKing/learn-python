#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-26 11:50:05
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-26 11:51:53

# err_raise.py
class FooError(ValueError):
	pass


def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10 / n

foo('0')