import joblib
import numpy as np

def model(input_data):
    model = joblib.load('model.pkl')
    input_data = np.array(input_data).reshape(1, -1)

    return model.predict(input_data)
