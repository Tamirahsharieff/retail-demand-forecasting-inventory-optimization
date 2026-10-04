from prophet import Prophet


def create_prophet_model(holidays=None):
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False,
        holidays=holidays
    )

    return model