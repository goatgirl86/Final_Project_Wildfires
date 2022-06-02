import joblib



def custome_transfer_func(test_data):

    
    print("*******")
    print(type(test_data))

    X = test_data.values
    
    
# Fit the StandardScaler

    X_scaler = joblib.load("X_scaler.save")
    X_scaled = X_scaler.transform(X)
# Scale the data
    
    return(X_scaled)
    



