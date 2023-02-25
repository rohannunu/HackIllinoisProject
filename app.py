from flask import Flask, request, jsonify, render_template
import time
app = Flask(__name__)

@app.route('/getMostSim')
def index():
    x = int(request.args.get('x'))
    return {
        "x":str(x+1)
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)


    