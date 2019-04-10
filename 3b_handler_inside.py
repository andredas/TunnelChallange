from flask import Flask
from flask import request
import logging
import requests
import sys
app = Flask(__name__)


@app.route('/3b_handler_inside', methods = ['POST'])
def action():
    #get message
    command = request.get_json()

    if command['action'] == 0 :
        app.logger.error('camera left')
        return"camera 0"
    elif command['action'] == 1 :
        app.logger.error('camera right')
        return "camera 1"
    elif command['action'] == 'warning':
        app.logger.error('light 100%')
        data ={'status': 2}
        r = requests.post(url='http://127.0.0.1:5004/verlichting', json=data)
        return "light 100"
    elif command['action'] == 'warning_over':
        app.logger.error('light normal')
        data = {'status': 1}
        r = requests.post(url='http://127.0.0.1:5004/verlichting', json=data)
        return "light normal"
    return "error"

