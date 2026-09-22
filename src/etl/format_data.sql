-- Day 4-7: Format date information
-- Retail Demand Forecasting Project

CREATE OR REPLACE TABLE
vocal-seeker-508915-g3.retail_demand_raw.sales_calendar_clean
AS

SELECT
  item_id,
  dept_id,
  cat_id,
  store_id,
  state_id,
  d,

  -- Convert calendar date into standard DATE format
  SAFE_CAST(date AS DATE) AS date,

  wm_yr_wk,
  weekday,
  wday,
  month,
  year,
  snap_CA,
  event_name_1,
  event_type_1,
  event_name_2,
  event_type_2

FROM
vocal-seeker-508915-g3.retail_demand_raw.sales_calendar;