import pandas as pd
import numpy as np
from imblearn.ensemble import EasyEnsembleClassifier
from sklearn.preprocessing import StandardScaler
import json


class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """

    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32,
                              np.float64)):
            return float(obj)
        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def custome_transfer_func(test_data):

    
    # standized scale
    # Create a StandardScaler instance
    ss = StandardScaler()

    X = test_data[["state", "discovery_month",
                   "Temp_pre_7", "Wind_pre_7", "Hum_pre_7"]]

    print("********")
    print(X)
# Fit the StandardScaler
    X_scaler = ss.fit_transform(X)

# Scale the data
    #X_test_scaled = X_scaler.transform(X_scaler)
    return(X_scaler)
    #return(json.dumps(X_scaler, cls=NumpyEncoder))



