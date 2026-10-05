import pandas as pd
import numpy as np


def evaluate_lightgbm(forecast_file):
    df = pd.read_csv(forecast_file)

    actual = df["actual_sales"]
    predicted = df["predicted_sales"]

    mae = np.mean(np.abs(actual - predicted))
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))

    metrics = {
        "MAE": round(mae, 4),
        "RMSE": round(rmse, 4)
    }

    return metrics