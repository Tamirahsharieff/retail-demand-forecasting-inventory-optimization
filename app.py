import streamlit as st
import csv

# Page configuration
st.set_page_config(
    page_title="Retail Demand Forecasting",
    layout="wide"
)

# Title
st.title("📊 Retail Demand Forecasting & Inventory Optimization")

st.write(
    "Interactive dashboard for viewing demand forecasts."
)

# Forecast file
forecast_file = "data/processed/lightgbm_forecast_HOBBIES_1_001.csv"

# Read CSV without pandas
rows = []

with open(forecast_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        rows.append(row)

# Forecast section
st.subheader("30-Day Demand Forecast")

# Display forecast data without pandas
if rows:
    headers = rows[0].keys()

    table = "| " + " | ".join(headers) + " |\n"
    table += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    for row in rows[:30]:
        table += "| " + " | ".join(str(row[h]) for h in headers) + " |\n"

    st.markdown(table)

else:
    st.warning("No forecast data found.")