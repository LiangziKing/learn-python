#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-23 16:45:51
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-23 16:47:18

class Student(object):
	def __init__(self, name):
		self.name = name

	def __call__(self):
		print('My name is %s.' % self.name)

s = Student('Michael')
s()