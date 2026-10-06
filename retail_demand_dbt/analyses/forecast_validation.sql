SELECT
    COUNT(*) AS total_rows,
    COUNTIF(date IS NULL) AS null_dates,
    COUNTIF(actual_sales IS NULL) AS null_actual_sales,
    COUNTIF(predicted_sales IS NULL) AS null_predictions,
    COUNTIF(predicted_sales < 0) AS negative_predictions,
    AVG(predicted_sales) AS avg_predicted_sales
FROM vocal-seeker-508915-g3.m5_retail.lightgbm_forecast;