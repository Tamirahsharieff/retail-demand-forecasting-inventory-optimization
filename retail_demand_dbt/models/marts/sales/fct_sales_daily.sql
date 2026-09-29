SELECT
    s.item_id,
    s.dept_id,
    s.cat_id,
    s.store_id,
    s.state_id,
    c.date,
    c.wm_yr_wk,
    c.wday,
    c.month,
    c.year,
    s.sales
FROM {{ ref('int_sales_daily') }} AS s
JOIN {{ ref('stg_calendar') }} AS c
    ON s.day = c.d