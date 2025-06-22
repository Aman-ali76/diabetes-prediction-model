import streamlit as st
from src.header import Header
from src.sidebar import Sidebar
from src.prediction import Prediction
from src.result import Result

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Diabetes Prediction App",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Initialize components
    header = Header()
    sidebar = Sidebar()
    prediction = Prediction("model/diabetes_model.pkl")
    result = Result()

    # Display header
    header.display()

    # Display sidebar (no theme selection needed)
    sidebar.display()

    # Get user input and make prediction
    input_data = prediction.get_user_input()
    if input_data is not None:
        try:
            prediction_result = prediction.make_prediction(input_data)
            result.show(prediction_result)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please check your input values and try again.")

if __name__ == "__main__":
    main()