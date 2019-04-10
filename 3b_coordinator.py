from flask import Flask
from flask import request
import logging
import requests
import json
#from __future__ import print_function # In python 2.7
import sys

app = Flask(__name__)


@app.route('/t', methods = ['POST'])
def MMI_handler():
    #get message
    command = request.get_json()
    app.logger.error('received commando')
    if command['type'] == "tunnel":
        if command['action'] == 0:
            data = {
                'action': 'open_tunnel'
            }
            r = requests.post(url = 'http://127.0.0.1:5002/3b_handler_outside', json = data)
        elif command['action'] == 1:
            data = {
                'action': 'warning'
            }
            r = requests.post(url='http://127.0.0.1:5002/3b_handler_outside', json=data)
            r = requests.post(url='http://127.0.0.1:5001/3b_handler_inside', json=data)
            return r.text
        elif command['action'] == 2:
            data = {
                'action': 'close_tunnel'
            }
            r = requests.post(url='http://127.0.0.1:5002/3b_handler_outside', json=data)
        elif command['action'] == 3:
            data = {
                'action': 'warning_over'
            }
            r = requests.post(url='http://127.0.0.1:5002/3b_handler_outside', json=data)
            r = requests.post(url='http://127.0.0.1:5001/3b_handler_inside', json=data)
            return r.text
    elif command['type'] == "cctv":
        data = {'action' : command['action']}
        r = requests.post(url='http://127.0.0.1:5001/3b_handler_inside', json=data)
        return r.text
    return "error"
