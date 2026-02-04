import pandas as pd
import numpy as np

def generate_traffic_data(n=8000, seed=42):
    np.random.seed(seed)

    df = pd.DataFrame({
        "hour_of_day": np.random.randint(0, 24, n),
        "day_of_week": np.random.randint(0, 7, n),
        "traffic_density": np.random.uniform(0.1, 1.0, n),
        "num_vehicles": np.random.randint(20, 500, n),
        "road_capacity": np.random.randint(200, 600, n),
        "weather_score": np.random.uniform(0.5, 1.0, n),  # 1 = clear
        "incident_reported": np.random.choice([0, 1], n, p=[0.9, 0.1])
    })

    # Speed decreases with congestion
    df["avg_speed"] = (
        80
        - 40 * df["traffic_density"]
        - 15 * df["incident_reported"]
        + 10 * df["weather_score"]
        - 0.05 * df["num_vehicles"]
        + np.random.normal(0, 3, n)
    )

    # Delay increases with congestion
    df["traffic_delay"] = (
        2
        + 25 * df["traffic_density"]
        + 10 * df["incident_reported"]
        - 5 * df["weather_score"]
        + 0.03 * df["num_vehicles"]
        + np.random.normal(0, 2, n)
    )

    return df

if __name__ == "__main__":
    df = generate_traffic_data()
    df.to_csv("data/traffic_data.csv", index=False)