from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the model once when the application starts
model = joblib.load('model.pkl')

app = Flask(__name__)

def get_prediction(data):
    """Extracts features and returns a personality prediction."""
    try:
        # Extract features from the input data
        personal_data = [
            data.get("Time_spent_Alone"),
            data.get("Stage_fear"),
            data.get("Social_event_attendance"),
            data.get("Going_outside"),
            data.get("Drained_after_socializing"),
            data.get("Friends_circle_size"),
            data.get("Post_frequency")
        ]

        # Ensure all features are present
        if any(x is None for x in personal_data):
            return {'error': 'Missing one or more required fields'}, 400

        # Convert to numpy array and reshape for the model
        personal_data = np.array(personal_data).reshape(1, -1)
        
        # Make the prediction
        prediction = model.predict(personal_data)

        # Return the personality type
        if prediction[0] == 1:
            return {'Personality': 'Introvert'}, 200
        else:
            return {'Personality': 'Extrovert'}, 200
            
    except Exception as e:
        return {'error': str(e)}, 500

@app.route('/', methods=['GET'])
def welcome():
    """A simple endpoint to confirm the server is running."""
    return "You are ON Server"

@app.route('/personality', methods=['POST'])
def process_personality():
    """Processes personality data from JSON or form data."""
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    result, status_code = get_prediction(data)
    return jsonify(result), status_code

if __name__ == '__main__':
    app.run(debug=True)
