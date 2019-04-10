from flask import Flask
from flask import request
import logging
#from __future__ import print_function # In python 2.7
import sys
app = Flask(__name__)


@app.route('/3B', methods = ['POST'])
def MMI_handler():
    #get message
    command = request.get_json()

    if command['type'] == "tunnel" :
        if command['action'] == 0 :
            data = {
                'action': 'open_tunnel'
            }
            r = requests.post(url = 'http://127.0.0.1:5000/3b_handler_outside', json = data)
        elif command['action'] == 1:
            data = {
                'action': 'warning'
            }
            r = requests.post(url='http://127.0.0.1:5000/3b_handler_outside', json=data)
            r = requests.post(url='http://127.0.0.1:5000/3b_handler_inside', json=data)
        elif command['action'] == 2:
            data = {
                'action': 'close_tunnel'
            }
            r = requests.post(url='http://127.0.0.1:5000/3b_handler_outside', json=data)
        elif command['action'] == 3:
            data = {
                'action': 'warning_over'
            }
            r = requests.post(url='http://127.0.0.1:5000/3b_handler_outside', json=data)
            r = requests.post(url='http://127.0.0.1:5000/3b_handler_inside', json=data)
    elif command['type'] == "tunnel":
        if command['action'] == 0 :
            #do something
        elif command['action'] == 1 :
            #do something

@app.route('/postjson', methods = ['POST'])
#def printMsg():
    #app.logger.warning('testing warning log')
#    app.logger.error('testing error log')
#    app.logger.info('testing info log')
#    return "Check your console"
def postJsonHandler():
    #print(request.is_json)
    content = request.get_json()
    #print(content)
    #app.logger.info('test')
    # #print('This is error output', file=sys.stderr)
    app.logger.error(content['name'])
    return 'JSON posted'