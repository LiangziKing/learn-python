#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-22 16:03:24
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-22 16:05:27

# 计算1+2+3+...+100:
sum = 0
n = 1
while n <= 100:
	sum = sum + n
	n = n + 1
print(sum)

# 计算1x2x3x...x100:
acc = 1
n = 1
while n <= 100:
	acc = acc * n
	n = n + 1
print(acc)