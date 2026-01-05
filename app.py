import streamlit as st
import joblib
import numpy as np

# load model
model = joblib.load("weather_model.pkl")


st.title("Temperature Prediction 🌡️")

sunlight = st.number_input("Hours of Sunlight", value=5.0)
humidity = st.number_input("Humidity Level", value=50.0)

if st.button("Predict"):
    result = model.predict([[sunlight, humidity]])
    st.success(f"Predicted Temperature: {result[0]:.2f} °C")
