from flask import Flask,  request, jsonify
from model import model
import os


app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf'}

@app.route('/', methods=['GET'])
def welcome():
    return "You are ON Server"

@app.route('/personality', methods=['POST'])
def process_personality():
    if request.is_json:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing data in request'}), 400
        
        Time_spent_Alone = data.get("Time_spent_Alone")
        Stage_fear = data.get("Stage_fear")
        Social_event_attendance = data.get("Social_event_attendance")
        Going_outside = data.get("Going_outside")
        Drained_after_socializing = data.get("Drained_after_socializing")
        Friends_circle_size = data.get("Friends_circle_size")
        Post_frequency = data.get("Post_frequency")

        personal_data = [Time_spent_Alone, Stage_fear, Social_event_attendance, Going_outside, Drained_after_socializing, Friends_circle_size, Post_frequency]
        try:
            json_data = model(personal_data)
            return jsonify({'True_Score': json_data})
    
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    elif 'files' not in request.files:
        return jsonify({'error': 'No file uploaded in the request'}), 400

    Time_spent_Alone = request.form.get("Time_spent_Alone")
    Stage_fear = request.form.get("Stage_fear")
    Social_event_attendance = request.form.get("Social_event_attendance")
    Going_outside = request.form.get("Going_outside")
    Drained_after_socializing = request.form.get("Drained_after_socializing")
    Friends_circle_size = request.form.get("Friends_circle_size")
    Post_frequency = request.form.get("Post_frequency")

    personal_data = [Time_spent_Alone, Stage_fear, Social_event_attendance, Going_outside, Drained_after_socializing, Friends_circle_size, Post_frequency]

    results = []
    try:
        json_data = model(personal_data)
        results.append({
            'True_Score':json_data,
        })
            
    except Exception as e:
        results.append({
            "status": "error",
            "message": str(e)
        })
           

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)
