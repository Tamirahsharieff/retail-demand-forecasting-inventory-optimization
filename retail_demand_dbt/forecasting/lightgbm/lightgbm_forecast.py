import pandas as pd
import lightgbm as lgb

from .prepare_lightgbm_data import prepare_lightgbm_data


def create_lightgbm_model():
    params = {
        "objective": "regression",
        "learning_rate": 0.05,
        "num_leaves": 31,
        "seed": 42,
        "verbosity": -1
    }

    return params


def train_and_forecast(params, X_train, y_train, X_future):
    train_data = lgb.Dataset(
        X_train,
        label=y_train
    )

    model = lgb.train(
        params,
        train_data,
        num_boost_round=500
    )

    forecast = model.predict(X_future)

    return forecast


def run_lightgbm_forecast(sales_file, calendar_file, item_id):

    # Prepare data
    data = prepare_lightgbm_data(
        sales_file,
        calendar_file,
        item_id
    )

    # Features used by LightGBM
    features = [
        "day_of_week",
        "day_of_month",
        "week_of_year",
        "lag_1",
        "lag_7",
        "lag_28",
        "rolling_7",
        "rolling_28"
    ]

    X = data[features]
    y = data["sales"]

    # Time-based train/test split
    split = int(len(data) * 0.8)

    X_train = X.iloc[:split]
    X_test = X.iloc[split:]

    y_train = y.iloc[:split]
    y_test = y.iloc[split:]

    # Create and train model
    params = create_lightgbm_model()

    predictions = train_and_forecast(
        params,
        X_train,
        y_train,
        X_test
    )

    # Create forecast output
    forecast = pd.DataFrame({
        "date": data.iloc[split:]["date"].values,
        "actual_sales": y_test.values,
        "predicted_sales": predictions
    })

    return forecast