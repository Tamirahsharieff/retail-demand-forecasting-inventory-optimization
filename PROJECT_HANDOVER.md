Project Handover — Retail Demand Forecasting & Inventory Optimization

1. Project Overview

This project forecasts retail product demand and supports inventory planning using historical sales data, machine learning, SQL transformations, and an interactive dashboard.

2. Technology Stack

- Python and Pandas
- Google BigQuery
- SQL and dbt
- Prophet
- LightGBM
- Streamlit

3. Completed Work

Data Engineering

- Prepared the M5 retail forecasting dataset.
- Loaded and validated data in BigQuery.
- Created dbt staging and intermediate transformations and analytical models.

Forecasting

- Implemented a Prophet forecasting workflow.
- Developed a LightGBM forecasting model.
- Evaluated predictions using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
- Stored LightGBM forecast results in BigQuery.

Interactive Dashboard

- Connected Streamlit to BigQuery.
- Added date filters and a sales summary.
- Displayed actual versus predicted sales.
- Added a what-if price reduction scenario.
- Added inventory planning estimates.
- Enabled CSV export of displayed results.

4. Validation

The LightGBM forecast table was checked for missing dates, missing actual sales, missing predictions, and negative predictions. The validation query returned 3,821 rows with no issues in these checks.

The recorded model evaluation results were:

- MAE: 0.5965
- RMSE: 0.8450

5. Running the Dashboard

From the project root, activate the appropriate Python environment and run:

streamlit run app.py

Google Cloud authentication and BigQuery permissions are required.

6. Security and Access

- Do not commit service-account keys, passwords, or other private credentials.
- Grant BigQuery access only to authorized users.
- The dashboard currently runs locally unless separately deployed.

7. Limitations and Future Improvements

- Generate and store genuine future-date forecasts before presenting them as future demand.
- Improve store and category filtering when the required fields are available in the forecast table.
- Validate the price-scenario assumptions against historical price-response data.
- Test dashboard access and deployment configuration before production use.

8. Handover Status

The forecasting pipeline, BigQuery forecast storage, and interactive dashboard have been implemented. Final review includes confirming that the latest code is pushed to GitHub, checking access permissions, and verifying the dashboard's outputs.

Project Deliverables

- Raw retail dataset and data preparation workflow.
- BigQuery tables for retail sales and forecast results.
- dbt staging, intermediate, and mart models.
- Prophet and LightGBM forecasting scripts.
- Streamlit dashboard for sales analysis.
- Inventory optimization and reorder estimation features.
- Project documentation and setup instructions.