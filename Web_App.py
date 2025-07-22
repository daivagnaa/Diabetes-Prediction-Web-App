import numpy as np
import pickle
import streamlit as st

# Loading the saved model
loaded_model = pickle.load(open(r'E:\Data Science\Projects\02. Diabites Prediction\trained_model.sav', 'rb'))

# Creating a Function for Prediction
def predict_diabetes(input_data):

    input_data_as_numpy_array = np.asarray(input_data)
    # Reshaping the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Making the prediction
    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == 0:
        return "The person is not diabetic"
    else:
        return "The person is diabetic"
    
# Streamlit App
def main():
    st.title("Diabetes Prediction Web App")
    st.write("Enter the following details to predict diabetes:")

    # Getting Input data from the user
    Pregnancies = st.text_input("Enter number of Pregnancies",placeholder='0-20')
    Glucose = st.text_input("Enter Glucose Level", placeholder='0-200')
    BloodPressure = st.text_input("Enter Blood Pressure", placeholder='0-200')
    SkinThickness = st.text_input("Enter Skin Thickness", placeholder='0-100')
    Insulin = st.text_input("Enter Insulin Level", placeholder='0-500')
    BMI = st.text_input("Enter BMI", placeholder='0.0-50.0')
    DiabetesPedigreeFunction = st.text_input("Enter Diabetes Pedigree Function", placeholder='0.0-2.5')
    Age = st.text_input("Enter Age", placeholder='0-120')
    input_data = (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

    # Code for Prediction
    diagnosis = ''

    # Creating a Button for Prediction
    if st.button("Check Your Result"):
        diagnosis = predict_diabetes(input_data)

    st.success(diagnosis)
    st.write("Developed by: Daivagna Parmar")
    


if __name__ == '__main__':
    main()