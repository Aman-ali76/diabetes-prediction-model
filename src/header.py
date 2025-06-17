import streamlit as st

class Header:
    """
    Header Class
    ------------
    Purpose:
        Renders the main page title and description.
    """
    
    def display(self):
        """
        Displays the header content of the app.
        This includes the title and a brief description of the app's purpose.
        """
        st.title("Diabetes Prediction App")
        st.markdown("This app predicts whether a person is likely to have diabetes based on medical inputs using a trained ML model.")
