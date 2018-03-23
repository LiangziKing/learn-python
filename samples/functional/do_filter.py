#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-23 10:26:29
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-23 10:28:54

def is_odd(n):
	return n % 2 == 1

L = range(100)

print(list(filter(is_odd, L)))

def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))