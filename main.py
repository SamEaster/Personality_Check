import joblib
import numpy as np

model = joblib.load('model.pkl')
def final_model(input_data):
    input_data = np.array(input_data).reshape(1, -1)

    return model.predict(input_data)
