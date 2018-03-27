#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-27 15:02:23
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-27 15:06:57

def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[CONSUMER] Consuming %s ...' % n)
		r = '200 OK'

def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER] Producing %s ...' % n)
		r = c.send(n)
		print('[PRODUCER] Consumer return: %s' % r)
	c.close()

c = consumer()
produce(c)