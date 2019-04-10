from . import scriptVerlichting
from flask import Flask
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
app = Flask(__name__)
@app.route('/database/<lamp>/<type>/<info>')
def save_data(lamp, type, info):

    if type

    #info check

    db = myclient["mydatabase"]
    mycol = db["lighting_log"]

    mylist = [
      {"Lamp: ": lamp, "; Adjustment: ": type, "; New value: ": info}
    ]

    x = mycol.insert_many(mylist)

    return 1


@app.route('/get/<lamp>/<type>/')
def get_data(lamp, typeI):

# lamp check

# type check

    scriptVerlichting.get_info(lamp, typeI)

    return 1


@app.route('/status/<status>')
def set_status(status):
    if(scriptVerlichting.set_status(status)) == 1:
        print("succes")
        return 'Status %s' % status

    else:
        print("failure")
        print(status)
        return 'Invalid status'
