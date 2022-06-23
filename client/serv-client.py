from flask import Flask, jsonify, render_template, request
from redis import Redis
from random import*

app = Flask(__name__)
rd = Redis(host="redis", port=6379)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/recargar', methods=['POST'])
def _get_data():
    revolver = rd.getdel('rev')
    
    return revolver

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=4000, debug=True)
