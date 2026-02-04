import streamlit as st
from src.predict import predict_traffic

st.set_page_config(page_title="Traffic AI Dashboard", layout="wide")
st.title("🚦 AI Traffic Speed & Delay Predictor")

st.sidebar.header("Enter Traffic Conditions")

hour = st.sidebar.slider("Hour of Day", 0, 23, 8)
day = st.sidebar.slider("Day of Week", 0, 6, 2)
density = st.sidebar.slider("Traffic Density", 0.1, 1.0, 0.5)
vehicles = st.sidebar.slider("Number of Vehicles", 20, 500, 200)
capacity = st.sidebar.slider("Road Capacity", 200, 600, 400)
weather = st.sidebar.slider("Weather Score (1=Clear)", 0.5, 1.0, 0.9)
incident = st.sidebar.selectbox("Incident Reported", [0, 1])

input_data = {
    "hour_of_day": hour,
    "day_of_week": day,
    "traffic_density": density,
    "num_vehicles": vehicles,
    "road_capacity": capacity,
    "weather_score": weather,
    "incident_reported": incident
}

if st.button("Predict Traffic"):
    speed, delay = predict_traffic(input_data)
    st.success(f"🚗 Predicted Avg Speed: {speed:.2f} km/h")
    st.warning(f"⏳ Predicted Traffic Delay: {delay:.2f} minutes")