SELECT
    s.item_id,
    s.dept_id,
    s.cat_id,
    s.store_id,
    s.state_id,
    DATE_TRUNC(c.date, WEEK(MONDAY)) AS week_start,
    SUM(s.sales) AS weekly_sales
FROM {{ ref('int_sales_daily') }} AS s
JOIN {{ ref('stg_calendar') }} AS c
    ON s.day = c.d
GROUP BY
    s.item_id,
    s.dept_id,
    s.cat_id,
    s.store_id,
    s.state_id,
    week_start