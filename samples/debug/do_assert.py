#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-26 11:37:27
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-26 11:38:39

def foo(s):
	n = int(s)
	assert n != 0, 'n is zero'
	return 10 / n

def main():
	foo('0')

main()