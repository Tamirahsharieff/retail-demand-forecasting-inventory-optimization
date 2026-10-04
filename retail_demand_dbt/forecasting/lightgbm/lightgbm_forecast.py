import lightgbm as lgb
import pandas as pd


def create_lightgbm_model():
    model = lgb.LGBMRegressor(
        objective="regression",
        n_estimators=500,
        learning_rate=0.05,
        num_leaves=31,
        random_state=42
    )

    return model


def train_and_forecast(model, X_train, y_train, X_future):
    model.fit(X_train, y_train)

    forecast = model.predict(X_future)

    return forecast