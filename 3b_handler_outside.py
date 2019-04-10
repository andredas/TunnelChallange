from flask import Flask
from flask import request
import logging
import time
#from __future__ import print_function # In python 2.7
import sys
app = Flask(__name__)


@app.route('/3b_handler_outside', methods = ['POST'])
def action():
    #get message
    command = request.get_json()

    if command['action'] == 'open_tunnel' :
        app.logger.error('open border')
        time.sleep(1)
        app.logger.error('green light')
        time.sleep(1)
        app.logger.error('dim light')
        return"camera 0"
    elif command['action'] == 'warning':
        app.logger.error('blink yellow')
        return "warning"
    elif command['action'] == 'close_tunnel':
        app.logger.error('blink yellow light')
        time.sleep(1)
        app.logger.error('yellow light')
        time.sleep(1)
        app.logger.error('red light')
        time.sleep(1)
        app.logger.error('close border')
        return "light 100"
    elif command['action'] == 'warning_over':
        app.logger.error('light dimmed')
        return "light dimmed"
    return "error"

