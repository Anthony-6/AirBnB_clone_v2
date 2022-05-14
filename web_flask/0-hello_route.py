#!/usr/bin/python3
''' script that start a flask application '''


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    ''' display “Hello HBNB!” on flask web application '''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)