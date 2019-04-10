from flask import Flask
from traffic import Traffic

app = Flask(__name__)

@app.route('/trafficlight/red')
def red_light():
    trafficlight = Traffic()
    trafficlight.setStand(3)
    trafficlight.update_light()
    return 'Hello, World!'

@app.route('/trafficlight/yellow')
def amber_light():
    trafficlight = Traffic()
    trafficlight.setStand(1)
    trafficlight.update_light()
    return 'Hello, World!'


@app.route('/trafficlight/green')
def green_light():
    trafficlight = Traffic()
    trafficlight.setStand(0)
    trafficlight.update_light()
    return 'Hello, World!'
