import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

# Load the dataset
data = pd.read_csv(r'E:\engineraa2\ai\student_performance.csv')

# Assume columns: 'study_hours', 'attendance', 'assignments_completed', 'previous_grades', 'extracurricular'
X = data[['study_hours', 'attendance', 'assignments_completed', 'previous_grades', 'extracurricular']]
y = data['performance']  # Binary classification: 0 (poor), 1 (good)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, r'E:\engineraa2\ai\model.joblib')

# Verify that the model is saved correctly by loading it and making a sample prediction
try:
    loaded_model = joblib.load(r'E:\engineraa2\ai\model.joblib')
    sample_input = np.array([[5, 90, 8, 85, 1]])
    sample_prediction = loaded_model.predict(sample_input)
    print(f"Sample prediction: {sample_prediction[0]}")
    print("Model saved and verified successfully.")
except Exception as e:
    print(f"Error loading the model: {e}")

