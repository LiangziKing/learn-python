#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-23 17:00:10
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-23 17:03:20

class Fib(object):

	def __init__(self):
		self.a, self.b = 0, 1 # 初始化两个计数器a，b

	def __iter__(self):
		return self # 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b # 计算下一个值
		if self.a > 100000: # 退出循环的条件
			raise StopIteration();
		return self.a # 返回下一个值

for n in Fib():
	print(n)