from flask import Flask, request,  render_template
import json
import pred_country
app = Flask(__name__)


parameterList = ["Ladder", "Positive affect","Social support", "Freedom", "Corruption", "Generosity", "Log of GDP per capita", "Healthy life expectancy", "CO2 Emissions", "Population", "Yearly Change", "Density", "Land Area", "Urban Pop %"]

@app.route('/')
def index():
    return render_template("index.html", parameterList=parameterList, parameterListLen=len(parameterList))

@app.route('/getCountry', methods = ["POST","GET"])
def getCountry():
    model_input = []
    data = json.loads( request.form.get("parameters"))
    for param in parameterList:
        arg = data[param]
        model_input.append(int(arg) if arg else 0)
    country = pred_country.pred_country(model_input)
    return country

@app.route('/getProb', methods = ["POST", "GET"])
def getProb():
    model_input = []
    data = json.loads(request.form.get("parameters"))
    for param in parameterList:
        arg = data[param]
        model_input.append(int(arg) if arg else 0)
    map_of_prob = pred_country.pred_prob(model_input)
    return map_of_prob
                                

@app.route('/getCountryImage', methods = ["POST", "GET"])
def getCountryImage():
    model_input = []
    data = json.loads(request.form.get("parameters"))
    for param in parameterList:
        arg = data[param]
        model_input.append(int(arg) if arg else 0)
    
    
    bytestream = pred_country.pred_prob(model_input)
    return bytestream     

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True) #TODO: change


    