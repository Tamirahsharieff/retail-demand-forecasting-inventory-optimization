import math

import pandas as pd
import streamlit as st
from google.cloud import bigquery


# --------------------------------------------------
# Page settings
# --------------------------------------------------
st.set_page_config(
    page_title="Retail Demand Forecasting",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# BigQuery configuration - TAMIRAH'S PROJECT
# --------------------------------------------------
PROJECT_ID = "vocal-seeker-508915-g3"

TABLE_ID = (
    "vocal-seeker-508915-g3."
    "m5_retail.lightgbm_forecast"
)


# --------------------------------------------------
# Dashboard title
# --------------------------------------------------
st.title("📊 Retail Demand Forecasting & Inventory Optimization")

st.write(
    "Interactive dashboard to analyze retail sales, "
    "compare LightGBM predictions, simulate pricing scenarios, "
    "and estimate inventory requirements."
)


# --------------------------------------------------
# Load forecast data from BigQuery
# --------------------------------------------------
@st.cache_data(ttl=300)
def load_forecast_data():
    client = bigquery.Client(project=PROJECT_ID)

    query = f"""
        SELECT
            date,
            SUM(actual_sales) AS actual_sales,
            SUM(predicted_sales) AS predicted_sales
        FROM {TABLE_ID}
        WHERE date IS NOT NULL
        GROUP BY date
        ORDER BY date
    """

    df = client.query(query).to_dataframe()

    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])

    return df


# --------------------------------------------------
# Handle BigQuery errors
# --------------------------------------------------
try:
    df = load_forecast_data()

except Exception as e:
    st.error("Unable to load forecast data from BigQuery.")
    st.error(str(e))
    st.info(
        "Check your Google Cloud authentication, project ID, "
        "dataset, table, and permissions."
    )
    st.stop()

if df.empty:
    st.warning("No forecast data found in BigQuery.")
    st.stop()

st.success("Forecast data loaded successfully from BigQuery!")


# --------------------------------------------------
# Sidebar filters
# --------------------------------------------------
st.sidebar.header("Dashboard Filters")

if st.sidebar.button("🔄 Refresh BigQuery Data"):
    load_forecast_data.clear()
    st.rerun()

st.sidebar.subheader("Date Range Filter")

min_date = df["date"].min().date()
max_date = df["date"].max().date()

selected_dates = st.sidebar.date_input(
    "Select date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

filtered_df = df.copy()

if isinstance(selected_dates, (tuple, list)):
    if len(selected_dates) == 2:
        start_date, end_date = selected_dates

        filtered_df = filtered_df[
            (filtered_df["date"].dt.date >= start_date)
            & (filtered_df["date"].dt.date <= end_date)
        ]

if filtered_df.empty:
    st.warning("No records found for the selected date range.")
    st.stop()


# --------------------------------------------------
# Display options
# --------------------------------------------------
st.sidebar.subheader("Display Options")

max_records = min(100, len(filtered_df))
default_records = min(10, max_records)

record_limit = st.sidebar.slider(
    "Number of records to display",
    min_value=1,
    max_value=max_records,
    value=default_records
)

st.sidebar.caption(
    "The table and chart display the most recent "
    "records in the selected date range."
)

display_df = (
    filtered_df
    .sort_values("date")
    .tail(record_limit)
    .copy()
)


# --------------------------------------------------
# Sales summary
# --------------------------------------------------
st.subheader("📌 Sales Summary")

actual_total = filtered_df["actual_sales"].sum()
predicted_total = filtered_df["predicted_sales"].sum()

mae = (
    filtered_df["actual_sales"]
    .sub(filtered_df["predicted_sales"])
    .abs()
    .mean()
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Actual Sales",
    f"{actual_total:,.0f}"
)

col2.metric(
    "Total Predicted Sales",
    f"{predicted_total:,.2f}"
)

col3.metric(
    "Mean Absolute Error (MAE)",
    f"{mae:.4f}"
)

st.caption(
    "MAE is the average absolute difference between actual "
    "and predicted daily sales. Lower values indicate "
    "smaller prediction errors."
)


# --------------------------------------------------
# Demand forecast table
# --------------------------------------------------
st.subheader("📋 Demand Forecast")

st.dataframe(
    display_df,
    width="stretch",
    hide_index=True
)


# --------------------------------------------------
# Actual vs predicted chart
# --------------------------------------------------
st.subheader("📈 Actual vs Predicted Sales")

chart_data = display_df.set_index("date")[
    ["actual_sales", "predicted_sales"]
]

st.line_chart(chart_data, width="stretch")


# --------------------------------------------------
# What-if price scenario
# --------------------------------------------------
st.divider()

st.subheader("💰 What-If Price Scenario")

st.write(
    "Estimate how a price reduction could affect demand. "
    "This is an assumption-based simulation, not a model "
    "trained on historical price-response data."
)

scenario_col1, scenario_col2 = st.columns(2)

with scenario_col1:
    price_reduction = st.slider(
        "Simulated price reduction (%)",
        min_value=0,
        max_value=30,
        value=10,
        step=1
    )

with scenario_col2:
    elasticity = st.slider(
        "Assumed demand elasticity",
        min_value=0.0,
        max_value=3.0,
        value=1.5,
        step=0.1
    )

baseline_demand = max(
    0.0,
    float(filtered_df["predicted_sales"].mean())
)

demand_increase_pct = (price_reduction / 100) * elasticity

scenario_demand = baseline_demand * (1 + demand_increase_pct)

additional_units = scenario_demand - baseline_demand

price_col1, price_col2, price_col3 = st.columns(3)

price_col1.metric(
    "Baseline Average Daily Demand",
    f"{baseline_demand:.2f} units"
)

price_col2.metric(
    "Scenario Daily Demand",
    f"{scenario_demand:.2f} units",
    delta=f"{demand_increase_pct * 100:.1f}%"
)

price_col3.metric(
    "Estimated Additional Units/Day",
    f"{additional_units:.2f}"
)

st.caption(
    "Assumption: a price reduction increases demand according "
    "to the selected elasticity. Actual demand may differ."
)


# --------------------------------------------------
# Inventory optimization
# --------------------------------------------------
st.divider()

st.subheader("📦 Inventory Optimization")

st.write(
    "Estimate target stock and suggested reorder quantity "
    "using predicted demand, supplier lead time, and safety stock."
)

inventory_col1, inventory_col2, inventory_col3 = st.columns(3)

with inventory_col1:
    current_stock = st.number_input(
        "Current inventory (units)",
        min_value=0,
        value=0,
        step=1
    )

with inventory_col2:
    lead_time = st.number_input(
        "Supplier lead time (days)",
        min_value=1,
        value=7,
        step=1
    )

with inventory_col3:
    safety_days = st.number_input(
        "Safety stock (days of demand)",
        min_value=0,
        value=3,
        step=1
    )

average_daily_demand = scenario_demand

lead_time_demand = average_daily_demand * lead_time

target_stock = math.ceil(
    average_daily_demand * (lead_time + safety_days)
)

suggested_reorder = max(
    0,
    target_stock - int(current_stock)
)

inv_col1, inv_col2, inv_col3, inv_col4 = st.columns(4)

inv_col1.metric(
    "Average Daily Demand",
    f"{average_daily_demand:.2f}"
)

inv_col2.metric(
    "Lead-Time Demand",
    f"{lead_time_demand:.2f}"
)

inv_col3.metric(
    "Target Stock",
    f"{target_stock} units"
)

inv_col4.metric(
    "Suggested Reorder",
    f"{suggested_reorder} units"
)

if suggested_reorder > 0:
    st.warning(
        f"Estimated replenishment needed: "
        f"{suggested_reorder} units."
    )
else:
    st.success(
        "Current stock meets or exceeds the estimated target stock."
    )

st.caption(
    "Planning estimate: target stock equals scenario demand "
    "per day multiplied by lead time plus safety-stock days. "
    "The estimate does not account for existing purchase orders, "
    "supplier constraints, or minimum order quantities."
)


# --------------------------------------------------
# Export results
# --------------------------------------------------
st.divider()

st.subheader("📥 Export Forecast Results")

export_df = display_df.copy()

export_df["scenario_daily_demand"] = scenario_demand
export_df["price_reduction_pct"] = price_reduction
export_df["assumed_elasticity"] = elasticity
export_df["target_stock_units"] = target_stock
export_df["current_stock_units"] = int(current_stock)
export_df["suggested_reorder_units"] = suggested_reorder

csv_data = export_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Forecast and Inventory CSV",
    data=csv_data,
    file_name="tamirah_retail_forecast_inventory.csv",
    mime="text/csv"
)

st.info(
    "This dashboard reads forecast records from BigQuery. "
    "The date filter selects records already stored in the table. "
    "Genuine future-demand forecasts must be generated and "
    "stored for future dates before they can appear here."
)


# --------------------------------------------------
# Footer
# --------------------------------------------------
st.divider()

st.caption(
    "Retail Demand Forecasting & Inventory Optimization | "
    "Powered by LightGBM, BigQuery and Streamlit"
)