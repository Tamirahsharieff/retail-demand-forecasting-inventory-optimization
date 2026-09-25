SELECT
    *
FROM {{ source('m5_raw', 'sell_prices') }}