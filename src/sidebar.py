import streamlit as st

class Sidebar:
    """
    Sidebar Class
    -------------
    Purpose:
        Displays sidebar content including:
        - Theme toggle (Light/Dark)
        - User instructions or app details
    """
    
    def display(self):
        """
        Displays the sidebar content of the app.
        This includes a theme toggle and instructions for the user.
        """
        st.sidebar.title("App Settings")
        

        # Sidebar Description
        st.sidebar.markdown("---")
        st.sidebar.markdown("**Instructions:**")
        st.sidebar.markdown("""
        - Enter the medical details in the prediction section.
        - Click **Predict** to see results.
        - All inputs are based on the PIMA Diabetes dataset.
        """)
        
