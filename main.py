#!/usr/bin/env python3
from flask import Flask, redirect, url_for, render_template, request, jsonify, send_from_directory, safe_join
import os,sys
import json

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = '\x99\x11\xfaa\xf6\x9f'

test_data  = [
    {
        'profile': 'img/cherprang.jpg',
        'owner': 'Paperplane0365',
        'title': 'ทริปสักอย่าง',
        'rating': 50,
        'route_img': 'img/route1.jpg'
    },
    {
        'profile': 'img/jennis.jpeg',
        'owner': 'lol',
        'title': 'ทริปสักอย่าง2',
        'rating': 90,
        'route_img': 'img/route2.jpg'
    },
    {
        'profile': 'img/pun.jpg',
        'owner': 'เครื่องบินกระดาษ 365',
        'title': 'สนามหลวง ทริปเดิน',
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
    app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
    app.run('0.0.0.0',port=8080,threaded=True)
else:
    app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')