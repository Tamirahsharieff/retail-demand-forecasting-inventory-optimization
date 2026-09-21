-- Day 4-7: Data Quality Checks
-- Retail Demand Forecasting Project


-- 1. Date quality check
SELECT
    COUNT(*) AS total_rows,
    COUNTIF(date IS NULL) AS null_dates,
    COUNT(DISTINCT date) AS unique_dates,
    MIN(date) AS start_date,
    MAX(date) AS end_date
FROM vocal-seeker-508915-g3.retail_demand_raw.sales_calendar;


-- 2. Sales volume quality check
SELECT
    COUNT(*) AS total_sales_values,
    COUNTIF(sales IS NULL) AS null_sales_values,
    COUNTIF(sales < 0) AS negative_sales_values,
    MIN(sales) AS minimum_sales,
    MAX(sales) AS maximum_sales
FROM vocal-seeker-508915-g3.retail_demand_raw.sales_train_validation
UNPIVOT(
    sales FOR day IN (d_1, d_2, d_3, d_4, d_5, d_6, d_7)
);


-- 3. Pricing quality check
SELECT
    COUNT(*) AS total_rows,
    COUNTIF(store_id IS NULL) AS null_store_id,
    COUNTIF(item_id IS NULL) AS null_item_id,
    COUNTIF(wm_yr_wk IS NULL) AS null_week,
    COUNTIF(sell_price IS NULL) AS null_price,
    COUNTIF(sell_price < 0) AS negative_prices,
    MIN(sell_price) AS minimum_price,
    MAX(sell_price) AS maximum_price
FROM vocal-seeker-508915-g3.retail_demand_raw.sell_prices;