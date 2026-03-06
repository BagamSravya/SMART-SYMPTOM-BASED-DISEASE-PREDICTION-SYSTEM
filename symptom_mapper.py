# symptom_mapper.py
import joblib
import numpy as np

# Load known symptoms from pickle
known_symptoms = joblib.load('known_symptoms.pkl')

def map_symptoms(user_symptoms):
    vector = [1 if symptom in user_symptoms else 0 for symptom in known_symptoms]
    return np.array(vector).reshape(1, -1)
