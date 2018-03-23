#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-23 13:20:31
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-23 13:23:01

class Animal(object):
	pass

class Dog(Animal):
	pass

class Husky(Dog):
	pass

a = Animal()
d = Dog()
h = Husky()

print('check a = Animal()...')
print('isinstance(a, Animal) =', isinstance(a, Animal))
print('isinstance(a, Dog) =', isinstance(a, Dog))
print('isinstance(a, Husky) =', isinstance(a, Husky))

print('check d = Dog()...')
print('isinstance(d, Animal) =', isinstance(d, Animal))
print('isinstance(d, Dog) =', isinstance(d, Dog))
print('isinstance(d, Husky) =', isinstance(d, Husky))

print('check h = Husky()...')
print('isinstance(h, Animal) =', isinstance(h, Animal))
print('isinstance(h, Dog) =', isinstance(h, Dog))
print('isinstance(h, Husky) =', isinstance(h, Husky))