from . import scriptVerlichting

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    print("test")
    return " World!"


@app.route('/status/<status>')
def set_status(status):
    # show the chosen status
    scriptVerlichting.set_status(1)
    return 'Status %s' % status

#hue link knop overbodig maken