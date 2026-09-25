SELECT
    item_id,
    dept_id,
    cat_id,
    store_id,
    state_id,
    d AS day,
    sales
FROM {{ ref('stg_sales_daily') }}