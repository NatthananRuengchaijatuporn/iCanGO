#!/usr/bin/env python3
from flask import Flask, redirect, url_for, render_template, request, jsonify, send_from_directory, safe_join
import os,sys
import json

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = '\x99\x11\xfaa\xf6\x9f'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 30

test_data  = [
    {
    	'id': 1,
        'profile': 'img/cherprang.jpg',
        'owner': 'โอนิกิรินั่งเครื่องบินกระดาษ',
        'title': 'เที่ยวกรุงคนเดียวก็เฟี้ยวได้',
        'rating': 100,
        'route_img': 'img/route1.jpg'
    },
    {
    	'id': 2,
        'profile': 'img/jennis.jpeg',
        'owner': 'หนูมาลีมีลูกแมวเหมียว',
        'title': 'เที่ยวเชียงใหม่ค่ะ',
        'rating': 90,
        'route_img': 'img/route2.jpg'
    },
    {
    	'id': 3,
        'profile': 'img/pun.jpg',
        'owner': 'ปุณณวิทย์ค่ะ',
        'title': 'เที่ยวสนามหลวง',
        'rating': 90,
        'route_img': 'img/route3.jpg'
    },
]

@app.route('/')
def index():
    return render_template('index.pug')

@app.route('/search')
def search():
    q = request.args.get('q')
    if q is None:
        return redirect(url_for('index'))
    return render_template('search_result.pug', location=q.title(), data=test_data)

@app.route('/route/<route>')
def route(route):
    return render_template('detail.pug')

if __name__ == '__main__':
    app.debug = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
    app.run('0.0.0.0',port=8080,threaded=True)
else:
    app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')