#!/usr/bin/python3
''' script that start a flask application '''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def stateandthecity(id=None):
    ''' return the states and the city'''
    states = storage.all(State)
    if id:
        key = '{}.{}'.format(State, id)
        if key in states:
            states = states[key]
        else:
            states = None
    else:
        states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def closeSession(self):
    ''' close the session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
