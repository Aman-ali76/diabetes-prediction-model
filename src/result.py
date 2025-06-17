import streamlit as st

class Result:
    """
    Result Class
    ------------
    Purpose:
        Displays the final prediction result on the main page.
        Supports themed coloring (Light/Dark).
    """

    def show(self, prediction: int, theme: str = "Light"):
        """
        Parameters:
            prediction : int
                The prediction result from the model (0 = Not Diabetic, 1 = Diabetic).
            theme : str
                The theme selected by the user ("Light" or "Dark").
        """
        if prediction == 1:
            message = "⚠️ The person is *likely Diabetic*."
            color = "#ff4b4b" if theme == "Light" else "#ff7b7b"
        else:
            message = "✅ The person is *not Diabetic*."
            color = "#28a745" if theme == "Light" else "#4dd07b"

        st.markdown(
            f"<div style='background-color:{color};padding:15px;border-radius:10px;'>"
            f"<h4 style='color:white;text-align:center;'>{message}</h4></div>",
            unsafe_allow_html=True
        )
