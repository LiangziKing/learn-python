#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-23 11:11:07
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-23 11:15:35

def main():
	for n in primes():
		if n < 1000:
			print(n)
		else:
			break

def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

if __name__ == '__main__':
	main()