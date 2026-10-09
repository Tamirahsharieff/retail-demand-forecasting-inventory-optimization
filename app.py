import os
import pandas as pd
import streamlit as st

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Retail Demand Forecasting",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------
# Dashboard Title
# -----------------------------------
st.title("Retail Demand Forecasting & Inventory Optimization")

st.write(
    "Demand analysis and machine learning predictions "
    "for inventory planning."
)

st.divider()

# -----------------------------------
# Load Forecast Data
# -----------------------------------
forecast_file = (
    "data/processed/lightgbm_forecast_HOBBIES_1_001.csv"
)

if not os.path.exists(forecast_file):
    st.error("Forecast CSV file not found. Please check the file path.")
    st.stop()

df = pd.read_csv(forecast_file)
# Forecast Filters
st.subheader("🔎 Forecast Filters")

col1, col2 = st.columns(2)

with col1:
    selected_store = st.selectbox(
        "Select Store",
        ["All Stores", "CA_1", "CA_2", "CA_3", "CA_4",
         "TX_1", "TX_2", "TX_3", "WI_1", "WI_2", "WI_3"]
    )

with col2:
    selected_category = st.selectbox(
        "Select Category",
        ["All Categories", "HOBBIES", "FOODS", "HOUSEHOLD"]
    )

st.info(
    f"Selected Store: {selected_store} | "
    f"Selected Category: {selected_category}"
)

required_columns = [
    "date",
    "actual_sales",
    "predicted_sales"
]

if not all(column in df.columns for column in required_columns):
    st.error("The forecast CSV is missing required columns.")
    st.stop()

df["date"] = pd.to_datetime(df["date"], errors="coerce")

df["actual_sales"] = pd.to_numeric(
    df["actual_sales"], errors="coerce"
)

df["predicted_sales"] = pd.to_numeric(
    df["predicted_sales"], errors="coerce"
)

df = df.dropna(subset=required_columns)
df = df.sort_values("date")

if df.empty:
    st.error("No valid forecast records are available.")
    st.stop()
    # Apply store and category filters
if selected_store != "All Stores" or selected_category != "All Categories":
    st.warning(
        "These filters are currently selections only. "
        "The loaded forecast CSV contains one item-level forecast, "
        "so store/category filtering requires matching store-level data."
    )

# -----------------------------------
# Calculate Evaluation Metrics
# -----------------------------------
mae = (
    df["actual_sales"] - df["predicted_sales"]
).abs().mean()

rmse = (
    (df["actual_sales"] - df["predicted_sales"]) ** 2
).mean() ** 0.5

# -----------------------------------
# Forecast Overview
# -----------------------------------
st.header("📌 Forecast Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Records",
        value=f"{len(df):,}"
    )

with col2:
    st.metric(
        label="Mean Absolute Error (MAE)",
        value=f"{mae:.4f}"
    )

with col3:
    st.metric(
        label="Root Mean Squared Error (RMSE)",
        value=f"{rmse:.4f}"
    )

st.caption(
    "Lower MAE and RMSE generally indicate more accurate predictions."
)

st.divider()

# -----------------------------------
# Prepare Daily Chart Data
# -----------------------------------
chart_data = (
    df.groupby("date")[
        ["actual_sales", "predicted_sales"]
    ]
    .mean()
    .sort_index()
)

# -----------------------------------
# Actual vs Predicted Sales
# -----------------------------------
st.subheader("📈 Actual vs Predicted Sales")

st.line_chart(
    chart_data.tail(90),
    height=420
)

st.caption(
    "Comparison of actual sales and LightGBM predictions "
    "over the most recent 90 days."
)

st.divider()

# -----------------------------------
# Demand Forecast Trend
# -----------------------------------
st.header("📉 Demand Forecast Trend")

st.line_chart(
    chart_data[["predicted_sales"]].tail(90),
    height=350
)

st.caption(
    "Daily average predicted sales over the most recent 90 days."
)

st.divider()

# -----------------------------------
# Forecast Data Preview
# -----------------------------------
st.header("📋 Forecast Data")

st.write("Preview of the first 30 records:")

display_df = df.copy()
display_df["date"] = display_df["date"].dt.strftime("%Y-%m-%d")

st.dataframe(
    display_df.head(30).rename(
        columns={
            "date": "Date",
            "actual_sales": "Actual Sales",
            "predicted_sales": "Predicted Sales"
        }
    ),
    use_container_width="stretch",
    hide_index=True
)

# -----------------------------------
# Download Forecast CSV
# -----------------------------------
csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Forecast CSV",
    data=csv_data,
    file_name="lightgbm_demand_forecast.csv",
    mime="text/csv"
)

# -----------------------------------
# Footer
# -----------------------------------
st.divider()

st.caption(
    "Retail Demand Forecasting & Inventory Optimization | "
    "Powered by LightGBM and Streamlit"
)