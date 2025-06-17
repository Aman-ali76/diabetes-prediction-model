import streamlit as st

class DisplayArea:
    """
    DisplayArea Class
    -----------------
    Purpose:
        Shows main app content like welcome text or introduction.
        Adjusts display styling based on selected theme.
    """

    def show(self, theme="Light"):
        """
        Displays the main content of the app.
        Parameters:
            theme (str): The selected theme for the app, either "Light" or "Dark".
        """
        if theme == "Dark":
            st.markdown(
                "<h2 style='color:#fafafa;'>Welcome to the Diabetes Prediction App</h2>", 
                unsafe_allow_html=True
            )
            st.markdown(
                "<p style='color:#d3d3d3;'>Use the sidebar to input patient details and predict diabetes outcome using a pre-trained ML model.</p>", 
                unsafe_allow_html=True
            )
        else:
            st.markdown("## Welcome to the Diabetes Prediction App")
            st.markdown(
                "Use the sidebar to input patient details and predict diabetes outcome using a pre-trained ML model."
            )
