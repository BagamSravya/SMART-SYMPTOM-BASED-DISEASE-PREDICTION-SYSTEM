from flask import Flask, render_template, request
import joblib
import pandas as pd
from symptom_mapper import map_symptoms

app = Flask(__name__)

# Load trained model and known symptoms
model = joblib.load('model.pkl')
known_symptoms = joblib.load('known_symptoms.pkl')

# Load supporting CSV datasets
desc_df = pd.read_csv('dataset/description.csv')
prec_df = pd.read_csv('dataset/precautions_df.csv')
med_df = pd.read_csv('dataset/medications.csv')
diet_df = pd.read_csv('dataset/diets.csv')

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_symptoms = request.form.getlist("symptoms")

        if len(user_symptoms) >= 3:
            input_vector = map_symptoms(user_symptoms)
            probabilities = model.predict_proba(input_vector)[0]
            top_index = probabilities.argmax()
            confidence = round(probabilities[top_index] * 100, 2)

            if confidence < 50:
                predicted_disease = "No disease predicted"
                result = {
                    "disease": predicted_disease,
                    "confidence": confidence
                }
            else:
                predicted_disease = model.classes_[top_index]

                # Fetch extra info
                description = desc_df[desc_df['Disease'] == predicted_disease]['Description'].values
                description = description[0] if len(description) else "Description not available"

                precautions = prec_df[prec_df['Disease'] == predicted_disease].values
                precautions = precautions[0][1:].tolist() if len(precautions) else ["No precautions found"]

                medications = med_df[med_df['Disease'] == predicted_disease].values
                medications = medications[0][1:].tolist() if len(medications) else ["No medications found"]

                diets = diet_df[diet_df['Disease'] == predicted_disease].values
                diets = diets[0][1:].tolist() if len(diets) else ["No diet recommendations"]

                doctor_search_link = f"https://www.google.com/search?q=doctors+for+{predicted_disease.replace(' ', '+')}+near+me"

                result = {
                    "disease": predicted_disease,
                    "confidence": confidence,
                    "description": description,
                    "precautions": precautions,
                    "medications": medications,
                    "diets": diets,
                    "doctor_link": doctor_search_link
                }

    return render_template("index.html", symptoms=known_symptoms, result=result)

if __name__ == "__main__":
    app.run(debug=True)
