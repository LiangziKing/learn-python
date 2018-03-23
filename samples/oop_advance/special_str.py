#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-23 17:03:33
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-23 17:05:19

class Student(object):

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' % self.name

	__repr__ = __str__

print(Student('Michael'))