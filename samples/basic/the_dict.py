#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-22 16:06:08
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-22 16:10:10

d = {
	'Michael': 95,
	'Bob': 75,
	'Tracy': 85
}
print('d[\'Michael\'] = ', d['Michael'])
print('d[\'Bob\'] = ', d['Bob'])
print('d[\'Tracy\'] = ', d['Tracy'])
print('d.get(\'Thomas\', -1) = ', d.get('Thomas', -1))