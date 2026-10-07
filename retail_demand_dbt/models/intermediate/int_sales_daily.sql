-- Intermediate dbt model for standardized long-format daily sales data
-- Converts M5 daily sales columns from wide format to long format.
-- This creates a daily-grain dataset suitable for time-series analysis and forecasting.

SELECT
    item_id,
    dept_id,
    cat_id,
    store_id,
    state_id,
    d AS day,
    sales
FROM {{ ref('stg_sales_daily') }}