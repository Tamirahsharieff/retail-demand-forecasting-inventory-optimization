# Day 4–7 Progress
## Retail Demand Forecasting & Inventory Optimization

### Completed Tasks

- Implemented data quality checks for the M5 dataset.
- Validated calendar date information.
- Checked sales data for:
  - NULL values
  - Negative sales values
  - Minimum sales
  - Maximum sales
- Checked pricing data for:
  - NULL store IDs
  - NULL item IDs
  - NULL week values
  - NULL sell prices
  - Negative prices
  - Minimum and maximum prices
- Verified the sales calendar contains:
  - 58,327,370 rows
  - 0 NULL dates
  - 1,913 unique dates
  - Start date: 2011-01-29
  - End date: 2016-04-24
- Verified sales data contains:
  - 213,430 sales values
  - 0 NULL sales values
  - 0 negative sales values
  - Minimum sales: 0
  - Maximum sales: 436
- Verified pricing data contains:
  - 6,841,121 rows
  - 0 NULL store IDs
  - 0 NULL item IDs
  - 0 NULL week values
  - 0 NULL sell prices
  - 0 negative prices
  - Minimum price: 0.01
  - Maximum price: 107.30

### SQL Files Created

- src/etl/data_quality_checks.sql
- src/etl/format_data.sql

### Data Formatting

Created the format_data.sql transformation script to standardize calendar date information and prepare the cleaned sales_calendar_clean table.

### GitHub

- Added and committed Day 4–7 data quality checks.
- Pushed changes successfully to the main branch.
- Added the Day 4–7 progress documentation.

### Status

Day 4–7 data quality validation is complete.

Date formatting SQL has been prepared and will be executed as the next ETL step.