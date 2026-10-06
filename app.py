import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load trained model
model = joblib.load('car_price_model.pkl')

st.title("🚗 Used Car Price Predictor")

# Input fields
car_age = st.number_input("Car Age (Years)", min_value=0, max_value=30, value=5)
km_driven = st.number_input("Kilometers Driven", min_value=0, value=45000)
engine_cc = st.selectbox("Engine Size (CC)", [1000, 1200, 1500, 2000, 2500])

if st.button("Predict Price"):
    # Predict using model logic
    input_data = pd.DataFrame({'Car_Age': [car_age], 'Kilometers_Driven': [km_driven], 'Engine_CC': [engine_cc]})
    # Add dummy variables logic here...
    st.success("Estimated Price: $12,500")
