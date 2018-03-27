#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-27 15:18:28
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-27 15:20:06

import os

from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('tempfile.1')
    os.remove('tempfile.2')
    os.remove('tempfile.3')
