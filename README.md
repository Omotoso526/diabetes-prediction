# diabetes-prediction
Diabetes Prediction Model

This project is a web application that predicts the likelihood of diabetes in a patient based on certain health metrics. The model was developed using a machine learning classifier and deployed using Streamlit for easy user interaction

# Deployed Application

You can interact with the deployed application here:

((https://omotoso526.github.io/diabetes-prediction/))

Overview

The diabetes prediction model is designed to provide a quick, data-driven assessment of diabetes risk based on the PIMA Indian Diabetes Database. The app allows users to input several health indicators, such as blood pressure and glucose levels, to get a prediction about their likelihood of having diabetes.

Features

*User-Friendly Interface: Streamlit app with an intuitive input form.

*Real-Time Prediction: Instantly calculates the likelihood of diabetes based on the inputs.

*ML Model: Uses a pre-trained machine learning model (logistic regression or similar classifier) to generate predictions.

Installation

* Clone the repository:

* git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app


Install the required packages: Make sure you have Python installed. Then install the dependencies using:

pip install -r requirements.txt

Run the Streamlit app: Launch the application by running the following command:

streamlit run app.py


Open in a browser: Once the app is running, 

go to http://localhost:8501 in your browser to access the application.

Usage

Open the app and fill in the required health metrics, such as:

    Glucose level
    Blood pressure
    Skin thickness
    BMI
    Age
    Insulin level

Click the "Predict" button to get the prediction.

The app will display the result as "The person is diabetic" or "The person has no diabetes".

**File Structure

    diabetes prediction webapp.py: Main Streamlit application file
    diabetes_model(l): Trained machine learning model used for predictions
    requirements.txt: List of dependencies for running the app
    README.md: Project documentation**


Dataset

The model was trained on the PIMA Indian Diabetes Database, a commonly used dataset for diabetes prediction research.

