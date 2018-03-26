#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-26 11:55:01
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-26 11:57:45

class Dict(dict):

	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value