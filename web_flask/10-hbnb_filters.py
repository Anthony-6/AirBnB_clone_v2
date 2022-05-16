#!/usr/bin/python3
''' script that start a flask application '''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def statewithoutthecity():
    '''Return state and amenities'''
    dicState = storage.all(State)
    dicAmenit = storage.all(Amenity)
    states = [dicState[k] for k, v in dicState.items()]
    amenities = [dicAmenit[k] for k, v in dicAmenit.items()]
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


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
