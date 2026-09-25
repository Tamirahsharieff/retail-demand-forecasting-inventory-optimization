SELECT
    *
FROM {{ source('m5_raw', 'calendar') }}