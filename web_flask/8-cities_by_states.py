#!/usr/bin/python3
''' script that start a flask application '''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def stateandthecity():
    '''return state and city of state'''
    return render_template('8-cities_by_states.html',
                           state=storage.all(State).values())


@app.teardown_appcontext
def closeSession(self):
    ''' close the session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
