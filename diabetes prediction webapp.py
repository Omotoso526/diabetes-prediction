# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:29:59 2024

@author: User
"""

import numpy as np
import streamlit as st
import pickle
import pandas as pd

loaded_model = pickle.load(open(r"C:/Users/User/Downloads/diabetes folder/diabetes_model.file", 'rb'))

#creating a function for prediction

def diabetes_prediction(input_data):
    
   
    #change the input_data to numpy array
    input_data_numpy = np.asarray(input_data)

    #reshape the array 
    input_data_reshape = input_data_numpy.reshape(1,-1)

 
    prediction =loaded_model.predict(input_data_reshape)
    prediction

    if prediction[0] == 0:
      return ("person has no diabetes")
    else:
      return ("person is diabetic")
  
    
  
def main():
    
   
    #giving a title
    st.title('Diabetes Prediction Web App')
    
    #getting the input data from the user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input("Skin Thicknes Value")
    Insulin = st.text_input("Insulin level")
    BMI = st.text_input(" BMI Value")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
    Age = st.text_input("Age of the person")
    
    
    #prediction code
    diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness,Insulin,BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
    
if __name__ == "__main__":
    main()

    