from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=["GET", 'POST'])
def index():
    return render_template("index1.html")


@app.route("/predict", methods=["GET", 'POST'])
def predict():
    output = "Your value here!"
    #If you have the user submit a form
    if request.method == 'POST':
        """
        state : state,
        discovery_month : discovery_month
        Temp_pre_7 : Temp_pre_7,
        Wind_pre_7 : Wind_pre_7,
        Hum_pre_7 : Hum_pre_7,
"""
        
        
        
        
        model = joblib.load('random_forest_4.joblib')
        
     
        state = request.json.get("state")
        discovery_month = request.json.get("discovery_month")
        Temp_pre_7 = request.json.get("Temp_pre_7")
        Wind_pre_7 = request.json.get("Wind_pre_7")
        Hum_pre_7 = request.json.get("Hum_pre_7")

        
        columns = ["state",
                   "discovery_month"
                   "Temp_pre_7",
                   "Wind_pre_7",
                   "Hum_pre_7",
                    
                   ]
        # test_data = [[education, urban, gender, engant, age, hand_orientation, religion, orientation, race, voted, married, family_size]]
        test_data = pd.DataFrame([[state,
                                    discovery_month,
                                    Temp_pre_7,
                                    Wind_pre_7,
                                    Hum_pre_7,
                                ]], columns=columns)
        pred = model.predict(test_data)

        print(test_data)
        print(pred)
        # return render_template('predictions.html', output=output)
        return {"Prediction": pred[0]}

    return render_template('predictions.html', output=output)


if __name__ == "__main__":
    app.run(debug=True)
