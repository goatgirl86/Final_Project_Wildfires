import pandas as pd
import numpy as np
import joblib



def custome_transfer_func(test_data):

    
    print("*******")
    print(type(test_data))
    #X_df = pd.DataFrame([test_data], columns=["state_no", "discovery_month_no", "Temp_pre_7", "Wind_pre_7", "Hum_pre_7"])
    X = test_data.values
    
    
# Fit the StandardScaler

    X_scaler = joblib.load("X_scaler.save")
    X_scaled = X_scaler.transform(X)
# Scale the data
    
    return(X_scaled)
    



