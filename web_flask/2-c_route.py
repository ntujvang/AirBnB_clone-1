#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
        return "HBNB"


@ap.route('/c/<text>')
def c(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
