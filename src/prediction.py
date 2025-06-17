import streamlit as st
import numpy as np
import pickle

class Prediction:
    """
    Prediction Class
    ----------------
    Purpose:
        Displays the input form to the user and uses the trained model
        to make a diabetes prediction.
    """

    def __init__(self, model_path='diabetes_model.pkl'):
        """
        Initializes the Prediction class with the given model path.
        """
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        """
        Loads and returns the trained model from a pickle file.
        """
        with open(self.model_path, 'rb') as file:
            model = pickle.load(file)
        return model

    def get_user_input(self):
        """
        Displays form to collect input data from user.

        Returns:
            np.array: Processed user input
        """
        with st.form("diabetes_form"):
            col1, col2 = st.columns(2)

            with col1:
                pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
                glucose = st.number_input("Glucose", min_value=0)
                blood_pressure = st.number_input("Blood Pressure", min_value=0)
                skin_thickness = st.number_input("Skin Thickness", min_value=0)

            with col2:
                insulin = st.number_input("Insulin", min_value=0)
                bmi = st.number_input("BMI", min_value=0.0, format="%.1f")
                diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
                age = st.number_input("Age", min_value=0, step=1)

            submitted = st.form_submit_button("Predict")

            if submitted:
                data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                                  insulin, bmi, diabetes_pedigree, age]])
                return data
        return None

    def make_prediction(self, input_data):
        """
        Uses the trained model to predict the outcome.

        Parameters:
            input_data : np.array
                User input for prediction

        Returns:
            int: 0 or 1
        """
        return self.model.predict(input_data)[0]
