import pandas as pd


def prepare_lightgbm_data(sales_file, calendar_file, item_id):
    sales = pd.read_csv(sales_file)
    calendar = pd.read_csv(calendar_file)

    # Select one product
    item = sales[sales["item_id"] == item_id].copy()

    # Get daily sales columns
    daily_columns = [
        col for col in item.columns
        if col.startswith("d_")
    ]

    # Convert wide format to long format
    daily_sales = item[
        ["item_id", "dept_id", "cat_id", "store_id", "state_id"]
        + daily_columns
    ].melt(
        id_vars=["item_id", "dept_id", "cat_id", "store_id", "state_id"],
        var_name="d",
        value_name="sales"
    )

    # Add calendar information
    daily_sales = daily_sales.merge(
        calendar[["d", "date", "wm_yr_wk", "wday", "month", "year"]],
        on="d",
        how="left"
    )

    # Convert date
    daily_sales["date"] = pd.to_datetime(daily_sales["date"])

    # Sort chronologically
    daily_sales = daily_sales.sort_values("date")

    # Create time-series features
    daily_sales["day_of_week"] = daily_sales["date"].dt.dayofweek
    daily_sales["day_of_month"] = daily_sales["date"].dt.day
    daily_sales["week_of_year"] = daily_sales["date"].dt.isocalendar().week.astype(int)

    # Lag features
    daily_sales["lag_1"] = daily_sales["sales"].shift(1)
    daily_sales["lag_7"] = daily_sales["sales"].shift(7)
    daily_sales["lag_28"] = daily_sales["sales"].shift(28)

    # Rolling features
    daily_sales["rolling_7"] = (
        daily_sales["sales"]
        .shift(1)
        .rolling(7)
        .mean()
    )

    daily_sales["rolling_28"] = (
        daily_sales["sales"]
        .shift(1)
        .rolling(28)
        .mean()
    )

    # Remove rows created by lag/rolling calculations
    daily_sales = daily_sales.dropna()

    return daily_sales