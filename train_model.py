import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from xgboost import XGBRegressor
from data_generator import generate_traffic_data

df = generate_traffic_data()

X = df.drop(["avg_speed", "traffic_delay"], axis=1)
y_speed = df["avg_speed"]
y_delay = df["traffic_delay"]

X_train, X_test, y_speed_train, y_speed_test = train_test_split(
    X, y_speed, test_size=0.2, random_state=42
)

_, _, y_delay_train, y_delay_test = train_test_split(
    X, y_delay, test_size=0.2, random_state=42
)

model_speed = XGBRegressor(n_estimators=300, max_depth=5, learning_rate=0.05)
model_delay = XGBRegressor(n_estimators=300, max_depth=5, learning_rate=0.05)

model_speed.fit(X_train, y_speed_train)
model_delay.fit(X_train, y_delay_train)

pred_speed = model_speed.predict(X_test)
pred_delay = model_delay.predict(X_test)

print("Speed R²:", r2_score(y_speed_test, pred_speed))
print("Delay R²:", r2_score(y_delay_test, pred_delay))
print("Delay MAE:", mean_absolute_error(y_delay_test, pred_delay))

joblib.dump(model_speed, "model_speed.pkl")
joblib.dump(model_delay, "model_delay.pkl")