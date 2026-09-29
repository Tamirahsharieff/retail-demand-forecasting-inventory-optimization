SELECT
    item_id,
    dept_id,
    cat_id,
    store_id,
    state_id,
    week_start,
    weekly_sales
FROM {{ ref('int_sales_weekly') }}