#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-22 15:57:54
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-22 15:59:45

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
age = int(input('Input your age: '))

if age >= 18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')