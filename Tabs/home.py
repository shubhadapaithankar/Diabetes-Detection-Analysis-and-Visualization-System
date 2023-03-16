"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Diabetes Detection, Analysis, & System")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:22px;">
            Diabetes is a health problem that lasts for a long time and affects the way your body processes food to produce energy. Unfortunately, there is currently no known cure for diabetes. However, making positive changes to your lifestyle, such as losing weight, eating a healthy diet, and staying active, can significantly reduce the impact of diabetes. With the help of this web application, you can predict the likelihood of a person having diabetes or being at risk of developing it in the future. The app analyzes various features and values using a Random Forest Classifier to make these predictions.
        </p>
    """, unsafe_allow_html=True)
