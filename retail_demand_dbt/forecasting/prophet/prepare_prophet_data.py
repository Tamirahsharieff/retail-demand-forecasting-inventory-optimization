import pandas as pd


def prepare_prophet_data(sales_file, calendar_file, item_id):
    sales = pd.read_csv(sales_file)
    calendar = pd.read_csv(calendar_file)

    item = sales[sales["item_id"] == item_id]

    daily_columns = [col for col in sales.columns if col.startswith("d_")]

    daily_sales = item[["item_id"] + daily_columns].melt(
        id_vars=["item_id"],
        var_name="d",
        value_name="y"
    )

    daily_sales = daily_sales.merge(
        calendar[["d", "date"]],
        on="d",
        how="left"
    )

    daily_sales = daily_sales.rename(columns={"date": "ds"})

    return daily_sales[["ds", "y"]]