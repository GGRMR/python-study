# -*- coding: utf-8 -*-
"""
Today
: URI 설계
@author: Park Jieun

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/name')
def helloName():
    return'Hello, name!'
    
@app.route('/name/<name>')
def helloName(name):
    return 'Hello,%s!'%name #함수인자와 같은 이름

@app.route('/<int:number>')
def helloNumber(number):
    return "it's %d"%number
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/score')
def score():
    return render_template('TestScore.html')

@app.route('/ScoreResult', methods=['GET','POST'])
def ScoreResult():
    if request.method == 'GET':
        return "it's GET"
    return render_template('ScoreResult.html',result=request.form)

@app.route('/word')
def word():
    return render_template('word.html')

@app.route('/wordResult', methods=['GET','POST'])
def wordResult():
    if request.method == 'GET':
        return "it's GET"
    return render_template('wordResult.html',result=request.form)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)

