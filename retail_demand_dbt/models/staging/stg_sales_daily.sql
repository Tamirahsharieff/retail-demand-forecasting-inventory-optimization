SELECT
    *
FROM {{ source('m5_raw', 'sales_daily') }}