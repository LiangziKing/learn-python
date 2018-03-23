#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-23 10:01:44
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-23 10:13:16

def each_ascii(s):
	for ch in s:
		yield ord(ch)
	return '%s chars' % len(s)

def yield_from(s):
	r = yield from each_ascii(s)
	print(r)

def main():
	for x in each_ascii('abc'):
		print(x) # => 'a', 'b', 'c'
	it = each_ascii('xyz')
	try:
		while True:
			print(next(it)) # => 'x', 'y', 'z'
	except StopIteration as s:
		print(s.value) # => '3 chars'
		
	# using yield from in main() will change main() from function to generator:
	# r = yield from each_ascii('hello')
	for ch in yield_from('hello'):
		pass


main()