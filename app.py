from flask import Flask, request, jsonify, render_template_string
import joblib
import numpy as np

model = joblib.load('model.pkl')

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personality Predictor</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center h-screen">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        <h1 class="text-2xl font-bold text-center text-gray-800 mb-6">Personality Predictor</h1>
        
        <!-- The form posts the data to the same URL ('/') -->
        <form action="/" method="POST">
            <div class="grid grid-cols-1 gap-4">
                <!-- Helper function to create form fields -->
                {% macro input(name, label, placeholder='Enter value 0-8') -%}
                <div class="mb-2">
                    <label for="{{ name }}" class="block text-sm font-medium text-gray-700">{{ label }}</label>
                    <input type="number" id="{{ name }}" name="{{ name }}" min="0" max="8" required
                           class="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                           placeholder="{{ placeholder }}">
                </div>
                {%- endmacro %}

                {{ input('Time_spent_Alone', 'Time Spent Alone') }}
                {{ input('Stage_fear', 'Stage Fear') }}
                {{ input('Social_event_attendance', 'Social Event Attendance') }}
                {{ input('Going_outside', 'Going Outside') }}
                {{ input('Drained_after_socializing', 'Drained After Socializing') }}
                {{ input('Friends_circle_size', 'Friends Circle Size') }}
                {{ input('Post_frequency', 'Social Media Post Frequency') }}
            </div>
            <div class="mt-6">
                <button type="submit"
                        class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    Predict Personality
                </button>
            </div>
        </form>

        <!-- Display the prediction result if it exists -->
        {% if prediction %}
        <div class="mt-6 p-4 rounded-md text-center" 
             style="background-color: {% if 'Introvert' in prediction %} #e0f2fe {% else %} #dcfce7 {% endif %}; 
                    color: {% if 'Introvert' in prediction %} #0c4a6e {% else %} #166534 {% endif %};">
            <h2 class="text-lg font-bold">Prediction Result:</h2>
            <p class="text-xl">{{ prediction }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

def get_prediction(data):
    try:
        personal_data = [
            data.get("Time_spent_Alone"),
            data.get("Stage_fear"),
            data.get("Social_event_attendance"),
            data.get("Going_outside"),
            data.get("Drained_after_socializing"),
            data.get("Friends_circle_size"),
            data.get("Post_frequency")
        ]

        if any(x is None for x in personal_data):
            return "Error: Missing one or more required fields"

        # Convert data to numeric types for the model
        personal_data_numeric = [float(x) for x in personal_data]
        
        personal_data_array = np.array(personal_data_numeric).reshape(1, -1)
        
        prediction = model.predict(personal_data_array)

        if prediction[0] == 1:
            return "You seem to be an Introvert!"
        else:
            return "You seem to be an Extrovert!"
            
    except Exception as e:
        return f"Error during prediction: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    if request.method == 'POST':
        form_data = request.form
        prediction_result = get_prediction(form_data)
    
    return render_template_string(HTML_TEMPLATE, prediction=prediction_result)

@app.route('/api/personality', methods=['POST'])
def api_predict():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    
    data = request.get_json()
    prediction_result = get_prediction(data)

    if "Error" in prediction_result:
        return jsonify({'error': prediction_result}), 400
        
    personality = "Introvert" if "Introvert" in prediction_result else "Extrovert"
    return jsonify({'Personality': personality})


if __name__ == '__main__':
    app.run(debug=True)
