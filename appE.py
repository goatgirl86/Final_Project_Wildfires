from calendar import month
from flask import Flask, jsonify, render_template, request
import joblib
import pandas as pd
from data_transfer import custome_transfer_func


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict/", methods=["GET", "POST"])
def predict():
    output = "Your value here!"
    #If you have the user submit a form
    if request.method == 'POST':
        """
        state : state,
        discovery_month : discovery_month,
        Temp_pre_7 : Temp_pre_7,
        Wind_pre_7 : Wind_pre_7,
        Hum_pre_7 : Hum_pre_7,
        """
        
        #'{"state":"AK","discovery_month":"1","Temp_pre_7":"12","Wind_pre_7":"13","Hum_pre_7":"14"}'
        model = joblib.load('model_joblib_ee.joblib')
        
        
        data = request.get_json()
        
        state = data["state"]
        
        
        discovery_month = data["discovery_month"]
        Temp_pre_7 = data["Temp_pre_7"]
        Wind_pre_7 = data["Wind_pre_7"]
        Hum_pre_7 = data["Hum_pre_7"]

        
        columns = ["state",
                   "discovery_month",
                   "Temp_pre_7",
                   "Wind_pre_7",
                   "Hum_pre_7",
                    
                   ]
        
        # test_data = [[education, urban, gender, engant, age, hand_orientation, religion, orientation, race, voted, married, family_size]]
        test_data = pd.DataFrame([[state,
                                    discovery_month,
                                    float(Temp_pre_7),
                                    float(Wind_pre_7),
                                    float(Hum_pre_7),
                                ]], columns=columns)
        #print(test_data)
        #print(pred)
        #print("*********")
        # Transfer test_data to normalized data
       
        normalized_data = custome_transfer_func(test_data)
        pred = model.predict(normalized_data)
        print("*********")
        print(pred)
        # return render_template('predictions.html', output=output)
        return jsonify({"Prediction": int(pred[0])})

    return render_template('predictions.html', output=output)

@app.route('/api/prediction')
def prediction():
    state = request.args.get('state')
    month = request.args.get("month")
    temp = request.args.get("temp")
    wind = request.args.get("wind")
    humid = request.args.get("humid")

    columns = ["state","discovery_month","Temp_pre_7","Wind_pre_7","Hum_pre_7",]
    test_data = pd.DataFrame(
        [[state, month, float(temp),float(wind),float(humid),]], 
        columns=columns
    )
    print("====")
    print(test_data)

    model = joblib.load('model_joblib_ee.joblib')
    normalized_data = custome_transfer_func(test_data)
    pred = model.predict(normalized_data)
   
    # return render_template('predictions.html', output=output)
    return jsonify({"Prediction": int(pred[0])})


if __name__ == "__main__":
    app.run(debug=True)
