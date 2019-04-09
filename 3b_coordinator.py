from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    return jsonify({
	    "type"		:	"cctv",
	    "state"		: 	1
    })