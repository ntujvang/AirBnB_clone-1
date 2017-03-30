#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states')
def states():
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route('/states/<uuid>')
def states_wid(uuid):
    states = storage.all("State")
    found = ""
    for ids in states:
        if ids == uuid:
            found = states[ids]
    return render_template("9-states.html", state=found)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
