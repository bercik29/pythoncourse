#!/usr/bin/python3

from flask import Flask, request, send_file, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route("/about")
def about():
    return "about page"

@app.route("/link")
def contact():
    username = request.args.get('name', 'Guest')
    age = request.args.get('age', 'too old')
    return render_template('index.html', name=username, age=age)

@app.route("/request", methods=['GET', 'POST'])
def req():
    name = request.args.get('name', 'Guest')
    age = request.args.get('age', 'too old')
    msg = f'Hello {name} you are {age}'
    return msg, 200, {'Contenty-Type' : 'Text/plain; utf-8'}

@app.route("/image")
def getimage():
    filename = 'sid.jpg'
    return send_file(filename, mimetype='image/jpg')

@app.route("/form", methods=['GET', 'POST'])
def formular():
    if request.method == 'GET':
        return render_template('index2.html')
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return render_template('index2.html', name=name, message=message)
    # 

@app.errorhandler(404)
def notfound(error):
    return render_template('404.html'), 404