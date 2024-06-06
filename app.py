from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('ai/model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assessment')
def assessment():
    return render_template('assessment.html')

@app.route('/learning-path')
def learning_path():
    return render_template('learning_path.html')

@app.route('/monitoring')
def monitoring():
    return render_template('monitoring.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([
        data['study_hours'],
        data['attendance'],
        data['assignments_completed'],
        data['previous_grades'],
        data['extracurricular']
    ]).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)