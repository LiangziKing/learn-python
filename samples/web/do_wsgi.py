#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-27 10:13:54
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-27 10:23:17

from wsgiref.simple_server import make_server

from hello import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

httpd.serve_forever()