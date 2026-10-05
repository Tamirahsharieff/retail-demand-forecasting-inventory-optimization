from prophet import Prophet


def create_prophet_model(holidays=None):
    model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False,
    holidays=holidays,
    changepoint_prior_scale=0.1
)

    return model


def train_and_forecast(model, data, periods=30):
    model.fit(data)

    future = model.make_future_dataframe(periods=periods)

    forecast = model.predict(future)

    return forecast