#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-27 10:13:23
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-27 10:17:29

def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]