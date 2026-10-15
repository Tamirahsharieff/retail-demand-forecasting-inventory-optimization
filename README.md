# retail-demand-forecasting-inventory-optimization
Retail demand forecasting and inventory optimization using Python, SQL, time-series forecasting, and interactive dashboards.

## Project Status

Project 3: Retail Demand Forecasting & Inventory Optimization

- GitHub repository initialized
- Python 3.11.9 virtual environment configured
- Project environment ready for Week 1 development
- # Retail-Demand-Forecasting-Inventory-Optimization

Retail demand forecasting and inventory optimization system using machine learning to predict product-level demand and recommend optimal stock levels, reducing overstock and stockouts.

## Dataset

This project uses the *M5 Forecasting – Accuracy* dataset from Kaggle, which contains daily unit sales data for thousands of products across multiple stores and states, along with calendar and pricing information.

Files used:
- calendar.csv — dates, events, and holidays
- sales_train_validation.csv — historical daily unit sales
- sell_prices.csv — product pricing by store and week

## Tech Stack

- *Python* — Pandas, PyArrow, python-dotenv
- *Google BigQuery* — data warehousing and querying
- *Machine Learning* (upcoming) — Prophet, LightGBM
- *Version Control* — Git & GitHub

## Project Plan

- *Week 1* — Set up local environment, load and explore the dataset
- *Week 2* — Clean and transform data (ETL pipeline)
- *Week 3* — Build and evaluate forecasting models
- *Week 4* — Inventory optimization logic and final reporting

## Folder Structure
data/         -> raw and processed datasets
src/etl/      -> ETL scripts
src/utils/    -> helper/utility functions
sql/          -> SQL queries
notebooks/    -> exploration and analysis notebooks
outputs/      -> results, reports, and visualizations

 "`n## Week 2 Progress - Day 4-6`n- Completed and validated the int_sales_daily dbt model.`n- Verified daily sales data transformation from staging to intermediate model.`n"

 Week 4: Interactive Dashboard & Reporting

Project Overview

Developed an interactive web dashboard using Streamlit to visualize retail demand forecasts and support inventory planning. The dashboard retrieves forecasting results from Google BigQuery.

Features Implemented

- BigQuery Integration: Loads actual sales and LightGBM predictions from the "m5_retail.lightgbm_forecast" table.
- Sales Summary: Displays total actual sales, total predicted sales, and Mean Absolute Error (MAE).
- Date Range Filter: Allows users to analyze forecasts within a selected date range.
- Demand Forecast Visualization: Displays forecast records in a table and compares actual sales with predicted sales using a line chart.
- What-If Price Scenario: Simulates the potential demand impact of a price reduction using an adjustable assumed demand elasticity.
- Inventory Optimization: Estimates target stock and suggested reorder quantities using predicted demand, supplier lead time, and safety-stock requirements.
- CSV Export: Allows users to download forecast results and inventory planning estimates.

Technologies Used

- Python
- Streamlit
- Pandas
- Google BigQuery
- LightGBM

How to Run the Dashboard

1. Activate the project's Python virtual environment.

2. Install the required dependencies from "requirements.txt".

3. Configure Google Cloud authentication and BigQuery permissions.

4. Run the application:
   
   "streamlit run app.py"

5. Open the local URL displayed in the terminal.

Notes

The price scenario and inventory calculations are planning estimates based on user-selected assumptions. They are not guarantees of actual demand or stock requirements. The dashboard displays forecast records already stored in BigQuery; future forecasts must be generated and stored separately.

How to Run the Dashboard

1. Activate the Python virtual environment.
2. Install the required dependencies using "pip install -r requirements.txt".
3. Start the Streamlit application using "streamlit run app.py".
4. Open the local URL displayed in the terminal.
5. Ensure Google Cloud authentication is configured to access BigQuery.

Project Workflow

1. Collect and prepare the M5 retail sales dataset.
2. Load raw data into Google BigQuery.
3. Transform and organize data using dbt.
4. Build demand forecasting models using Prophet and LightGBM.
5. Store forecast results in BigQuery.
6. Visualize sales trends through the Streamlit dashboard.
7. Use demand estimates to support inventory planning.