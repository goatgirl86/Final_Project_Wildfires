from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=["GET", 'POST'])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET", 'POST'])
def predict():
    output = "Your value here!"
    #If you have the user submit a form
    if request.method == 'POST':
        """
       fire_id : fire_id,
        fire_size : fire_size,
        fire_cause : fire_cause,
        latitude : latitude,
        longitude : longitude,
        state : state,
        discovery_month : discovery_month,
        Temp_pre_30 : ???,
        Temp_pre_15 : ???,
        Temp_pre_7 : ???,
        Wind_pre_30 : ???,
        Wind_pre_15 : ???,
        Wind_pre_7 : ???,
        Hum_pre_30 : ???,
        Hum_pre_15 : ???,
        Hum_pre_7 : ???,
        year : ???,
        putout_time : ???,
        fire_size_bin : ???
        
"""
        model = joblib.load('random_forest_4.joblib')
        
        fire_id = request.json.get("fire_id")
        fire_size = request.json.get("fire_size")
        fire_cause = request.json.get("fire_cause")
        latitude = request.json.get("latitude")
        longitude = request.json.get("longitude")
        state = request.json.get("state")
        discovery_month = request.json.get("discovery_month")
        Temp_pre_30 = request.json.get("???")
        Temp_pre_15 = request.json.get("???")
        Temp_pre_7 = request.json.get("???")
        Wind_pre_30 = request.json.get("???")
        Wind_pre_15 = request.json.get("???")
        Wind_pre_7 = request.json.get("???")
        Hum_pre_30 = request.json.get("???)
        Hum_pre_15 = request.json.get("???")
        Hum_pre_7 = request.json.get("???")
        year = request.json.get("???")
        putout_time = request.json.get("???")
        fire_size_bin = request.json.get("???")
        
        columns = ["fire_id",
                   "fire_size",
                   "fire_cause",
                   "latitude",
                   "longitude",
                   "state",
                   "discovery_month",
                   "Temp_pre_30",
                   "Temp_pre_15",
                   "Temp_pre_7",
                   "Wind_pre_30",
                  "Wind_pre_15",
                   "Wind_pre_7",
                   "Hum_pre_30",
                   "Hum_pre_15",
                   "Hum_pre_7",
                   "year",
                   "putout_time",
                   "fire_size_bin"]
        # test_data = [[education, urban, gender, engant, age, hand_orientation, religion, orientation, race, voted, married, family_size]]
        test_data = pd.DataFrame([[fire_id,
                                   fire_size,
                                   fire_cause,
                                   latitude,
                                   longitude,
                                   state,
                                   discovery_month,
                                   Temp_pre_30,
                                   Temp_pre_15,
                                   Temp_pre_7,
                                   Wind_pre_30,
                                   Wind_pre_15,
                                   Wind_pre_7,
                                   Hum_pre_30,
                                   Hum_pre_15,
                                   Hum_pre_7,
                                   year,
                                   putout_time,
                                   fire_size_bin]], columns=columns)
        pred = model.predict(test_data)

        print(test_data)
        print(pred)
        # return render_template('predictions.html', output=output)
        return {"Prediction": pred[0]}

    return render_template('predictions.html', output=output)


if __name__ == "__main__":
    app.run(debug=True)
