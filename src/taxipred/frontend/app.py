import streamlit as st
import requests

st.set_page_config(page_title="Taxi Price", layout="centered")

st.title("Taxi Price Predictor")

st.write("Enter your trip and get a price prediction.")

# Input columns
col1, col2 = st.columns(2)

with col1:
    distance = st.number_input("Distance (km)", min_value=1.0, max_value=70.0, value=10.0)
    time_of_day = st.selectbox("Time", ["Morning", "Afternoon", "Evening", "Night"])
    passengers = st.selectbox("Passengers", [1, 2, 3, 4])

with col2:
    day_of_week = st.selectbox("Day", ["Weekday", "Weekend"])
    traffic = st.selectbox("Traffic", ["Low", "Medium", "High"])
    weather = st.selectbox("Weather", ["Clear", "Snow", "Rain"])

# Predict button
if st.button("Calculate Price"):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={
                "trip_distance": distance,
                "time_of_day": time_of_day,
                "day_of_week": day_of_week,
                "passenger_count": passengers,
                "traffic_conditions": traffic,
                "weather": weather
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            price_original = result['predicted_price']
            st.balloons()

            st.success(f"Price: ${price_original:.2f} USD")
        else:
            st.error("Error getting prediction")
    except Exception as e:
        st.error(f"Connection error: {str(e)}")
