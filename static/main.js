parameterList = ["Ladder", "Positive affect","Social support", "Freedom", "Corruption", "Generosity", "Log of GDP per capita", "Healthy life expectancy", "CO2 Emissions", "Population", "Yearly Change", "Density", "Land Area", "Urban Pop %"]

function changeCountry(){
    obj = {};
    for (i in parameterList){
        param = parameterList[i]
        obj[param] = document.getElementById(param).value;
    }
    console.log(obj);
    $.post( "/getCountry",
    {"parameters":JSON.stringify(obj)},
    function(data, status){
        document.getElementById("my-country-header").innerHTML = "Your results are most similar to "+data+".";
      });
}

function getProbabilityCountry() {
    obj = {};
    for (i in parameterList) {
        param = parameterList[i]
        obj[param] = document.getElementById(param).value;
    }
    console.log(obj);
    $.post( "/getProb",
    {"parameters":JSON.stringify(obj)},
    function(data, status) {
        console.log(data);
    });
}