# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:25:14 2019

@author: samsung
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/register')
def score():
    return render_template('bookInfo.html')

@app.route('/books', methods=['GET','POST'])
def ScoreResult():
    if request.method == 'GET':
        return "it's GET"
    return render_template('ScoreResult.html',result=request.form)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
