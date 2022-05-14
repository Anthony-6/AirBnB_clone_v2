#!/usr/bin/python3
''' script that start a flask application '''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    ''' display “Hello HBNB!” on flask web application route / '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def second():
    ''' display HBNB on flask web application route /hbnb'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def third(text):
    ''' return C and text that come after the / in route /c/ and replace
        underscore with whitespace'''
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def fourth(text):
    ''' return C and text that come after the / in route /c/ and replace
        underscore with whitespace'''
    return 'Python %s' % text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
