from flask import Flask, request,  render_template, jsonify
import json
import pred_country
app = Flask(__name__)


parameterList = ["Ladder", "Positive affect","Social support", "Freedom", "Corruption", "Generosity", "Log of GDP per capita", "Healthy life expectancy", "CO2 Emissions", "Population", "Yearly Change", "Density", "Land Area", "Urban Pop %"]
totalAvailablePoints = 750

@app.route('/')
def index():
    return render_template("index.html", parameterList=parameterList, parameterListLen=len(parameterList))

@app.route('/getCountry', methods = ["POST","GET"])
def getCountry():
    model_input = []
    data =json.loads( request.form.get("parameters"))
    for param in parameterList:
        arg = data[param]
        model_input.append(int(arg) if arg else 0)
    country = pred_country.pred_country(model_input)
    return country


@app.route('/updatePointValue/', methods=["POST"])
def updateInternalPointValue():
    sumOfSliders = json.loads( request.form.get("totalVal"))
    return str(totalAvailablePoints - sumOfSliders)
       
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=False) #TODO: change


    