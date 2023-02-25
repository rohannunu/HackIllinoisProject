from flask import Flask, request, jsonify, render_template
import time
app = Flask(__name__)


parameterList = ["population", "pollution", "nature", "GDP"]

@app.route('/')
def index():
    return render_template("index.html", parameterList=parameterList)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)


    