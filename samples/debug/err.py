#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-26 11:32:11
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-26 11:34:18

# err.py
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	bar('0')

main()
