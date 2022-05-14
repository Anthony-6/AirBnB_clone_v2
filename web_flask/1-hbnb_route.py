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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
