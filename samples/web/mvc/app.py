#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiangziKing
# @E-mail: 1990818918@qq.com
# @Date:   2018-03-27 10:28:30
# @Last Modified by:   LiangziKing
# @Last Modified time: 2018-03-27 12:08:10

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.htm')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.htm')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.htm', username=username)
    return render_template('form.htm', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
