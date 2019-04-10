import cv2
from pymongo import MongoClient
import requests
from flask import Flask
import time
import datetime

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

import keyboard  # using module keyboard

client = MongoClient('mongodb://localhost:27017')
db = client['pymongo_test']

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)

url = 'http://root:root@192.168.3.40/axis-cgi/com/ptz.cgi'
presets = list()
pan = int()
tilt = int()
zoom = int()


def setpan(a):
    if a < -180:
        a = -180
    elif a > 180:
        a = 180
    global pan
    pan = a


def getpan():
    global pan
    return pan


def settilt(a):
    if a > 0:
        a = 0
    if a < -90:
        a = -90
    global tilt
    tilt = a


def getpan():
    global tilt
    return tilt


def setzoom(a):
    if a > 9999:
        a = 9999
    if a < 0:
        a = 0
    global zoom
    zoom = a


def getzoom():
    global zoom
    return zoom


def createlist(k):
    i = len(presets)
    if k + 1 > len(presets):
        while i in range(k + 1):
            presets.append(dict())
            i = len(presets)
    print(len(presets))


def definieerpreset(k, p, t, z):
    createlist(k)
    # if isinstance(presets[k], dict):
    presets[k] = {"pan": p, "tilt": t, "zoom": z}


definieerpreset(0, 90, -20, 0)
definieerpreset(1, -80, -10, 0)


@app.route('/settopreset/<s>')
def settopreset(s):
    k = int(s)
    pan = presets[k].get("pan")
    tilt = presets[k].get("tilt")
    zoom = presets[k].get("zoom")
    payload = {'camera': '1', 'pan': pan, 'tilt': tilt, 'zoom': zoom, 'imagerotation': '0'}
    r = requests.get(url, params=payload)
    return "done"


@app.route('/sethome')
def sethome():
    r = requests.get(
        'http://root:root@192.168.3.40/axis-cgi/com/ptz.cgi?camera=1&gotoserverpresetname=Home&timestamp=1554816422687')

    return "sethome"


@app.route('/setidentificatiecode/<code>')
def setidentificatiecode(code):
    posts = db.posts
    try:
        r = requests.get(
            'http://root:root@192.168.3.40/axis-cgi/operator/param_authenticate.cgi?action=update&Image.I0.Text.String=' + code)

        post_data = {
            'timestamp': ts,
            'state': 'INFO',
            'message': 'De identificatiecode is op '+code+' gezet'
        }

    except:
        posts = db.posts
        post_data = {
            'timestamp': ts,
            'state': 'ERROR',
            'message': 'De identificatiecode kan niet worden veranderd'
        }
    result = posts.insert_one(post_data)
    return "identificatiecode is veranderd naar "+code
# print('One post: {0}'.format(result.inserted_id))
# cap = cv2.VideoCapture('rtsp://root:root@192.168.3.40/axis-media/media.amp')


# cap.release()
# cv2.destroyAllWindows()

# payload = {'camera': '1', 'pan': pan, 'tilt': tilt, 'zoom': zoom, 'imagerotation': '0'}
# r = requests.get(url, params=payload)
# if keyboard.is_pressed('a'):  # if key 'q' is pressed
#     r = requests.get('http://root:root@192.168.3.40/axis-cgi/com/ptz.cgi?camera=1&continuouspantiltmove=-100,0&imagerotation=0')
# elif keyboard.is_pressed('d'):  # if key 'q' is pressed
#     r = requests.get('http://root:root@192.168.3.40/axis-cgi/com/ptz.cgi?camera=1&continuouspantiltmove=100,0&imagerotation=0')
# elif keyboard.is_pressed('w') :
#     r = requests.get('http://root:root@192.168.3.40/axis-cgi/com/ptz.cgi?camera=1&continuouspantiltmove=0,100&imagerotation=0')
# elif keyboard.is_pressed('s'):
#     r = requests.get('http://root:root@192.168.3.40/axis-cgi/com/ptz.cgi?camera=1&continuouspantiltmove=0,-100&imagerotation=0')
# elif keyboard.is_pressed('z'):
#     r = requests.get('http://root:root@192.168.3.40/axis-cgi/com/ptz.cgi?camera=1&continuouszoommove=100&imagerotation=0')
# elif keyboard.is_pressed('x'):
#     r = requests.get('http://root:root@192.168.3.40/axis-cgi/com/ptz.cgi?camera=1&continuouszoommove=-100&imagerotation=0')
# elif keyboard.is_pressed('q'):
#     break
# else:
#     r = requests.get('http://root:root@192.168.3.40/axis-cgi/com/ptz.cgi?camera=1&continuouspantiltmove=0,0&imagerotation=0')
#     r = requests.get('http://root:root@192.168.3.40/axis-cgi/com/ptz.cgi?camera=1&continuouzoommove=0&imagerotation=0')
#

# ret, frame = cap.read()
# cv2.imshow('frame',frame)
# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break
