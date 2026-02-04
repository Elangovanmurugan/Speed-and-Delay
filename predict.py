import joblib
import pandas as pd

model_speed = joblib.load("model_speed.pkl")
model_delay = joblib.load("model_delay.pkl")

def predict_traffic(data_dict):
    df = pd.DataFrame([data_dict])
    speed = model_speed.predict(df)[0]
    delay = model_delay.predict(df)[0]
    return speed, delay