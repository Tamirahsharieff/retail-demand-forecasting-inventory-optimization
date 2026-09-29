SELECT
    item_id,
    dept_id,
    cat_id,
    store_id,
    state_id,
    month_start,
    monthly_sales
FROM {{ ref('int_sales_monthly') }}