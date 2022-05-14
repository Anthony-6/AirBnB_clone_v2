#!/usr/bin/python3
''' script that start a flask application '''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def statewithoutthecity():
    '''return state and city of state'''
    return render_template('7-states_list.html',
                           state=storage.all(State).values())


@app.route('/states/<id>', strict_slashes=False)
def stateandthecity(id):
    ''' return the states and the city'''
    dic = storage.all(State)
    states = [dic[k] for k, v in dic.items() if v.id == id]
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def closeSession(self):
    ''' close the session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
