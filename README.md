# SMART SYMPTOM BASED DISEASE PREDICTION SYSTEM

## Overview

The **Smart Symptom Based Disease Prediction System** is a Machine Learning based web application that predicts possible diseases based on symptoms entered by the user.

The system uses a trained Machine Learning model to analyze symptoms and predict the most probable disease along with additional medical information such as description, precautions, medications, and diet recommendations.

This project aims to demonstrate how **Artificial Intelligence can assist in early disease prediction and healthcare awareness**.

---

## Features

* Predicts disease based on user-selected symptoms
* Displays prediction confidence score
* Provides disease description
* Suggests precautions to follow
* Recommends medications
* Provides diet recommendations
* Generates a Google search link to find doctors nearby
* Simple and user-friendly web interface

---

## Tech Stack

* **Python**
* **Flask**
* **Machine Learning**
* **Scikit-learn**
* **Pandas**
* **HTML**
* **CSS**

---

## Machine Learning Model

The system uses the **Multinomial Naive Bayes algorithm** to classify diseases based on symptoms.

The model is trained on a dataset containing multiple diseases and their associated symptoms.

Training is performed using the `train_model.py` script, which generates:

* `model.pkl` – Trained Machine Learning model
* `known_symptoms.pkl` – List of all symptoms used by the model

---

## Project Structure

```
SMART SYMPTOM BASED DISEASE PREDICTION SYSTEM/
│
├── app.py
├── train_model.py
├── symptom_mapper.py
├── model.pkl
├── known_symptoms.pkl
│
├── dataset/
│   ├── Training.csv
│   ├── description.csv
│   ├── precautions_df.csv
│   ├── medications.csv
│   ├── diets.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── screenshots/
│   ├── output screen1.png
│   ├── output screen2.png
│   └── output screen3.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Screenshots

### Application Output

![Output Screen 1](screenshots/output_screen_1.png)

![Output Screen 2](screenshots/output_screen_2.png)

![Output Screen 3](screenshots/output_screen_3.png)

---

## Installation and Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/SMART-SYMPTOM-BASED-DISEASE-PREDICTION-SYSTEM.git
```

---

### 2. Navigate to the project folder

```
cd SMART-SYMPTOM-BASED-DISEASE-PREDICTION-SYSTEM
```

---

### 3. Install required dependencies

```
pip install -r requirements.txt
```

---

### 4. Train the Machine Learning Model (Optional)

If you want to retrain the model:

```
python train_model.py
```

This will generate:

* `model.pkl`
* `known_symptoms.pkl`

---

### 5. Run the application

```
python app.py
```

---

### 6. Open the application in browser

```
http://127.0.0.1:5000
```

---

## How the System Works

1. User selects symptoms from the web interface.
2. Symptoms are converted into a numerical vector using the symptom mapper.
3. The trained Machine Learning model predicts the most probable disease.
4. The system calculates the prediction confidence.
5. If confidence is high enough, the system displays:

   * Disease name
   * Description
   * Precautions
   * Medications
   * Diet recommendations
6. A Google search link is provided to help the user find doctors nearby.

---

## Future Improvements

* Add more diseases and symptoms
* Improve model accuracy using advanced algorithms
* Add Explainable AI (XAI) for better model transparency
* Deploy the application online
* Improve UI with modern design

---

## Author

Developed as a Machine Learning project to demonstrate the use of AI in healthcare prediction systems.
