from flask import Flask
from flask import request
import logging
#from __future__ import print_function # In python 2.7
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
        return "light 100"
    elif command['action'] == 'warning_over':
        app.logger.error('light normal')
        return "light normal"
    return "error"

