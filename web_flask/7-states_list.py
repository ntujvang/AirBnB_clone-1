#!/usr/bin/python3
"""
python script to create a flask page that contains x amount of states
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """
    method to create a webpage that list states
    """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """
    method to tear down
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
