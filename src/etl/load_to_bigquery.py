from pathlib import Path

from google.cloud import bigquery


# Google Cloud project and BigQuery dataset
PROJECT_ID = "vocal-seeker-508915-g3"
DATASET_ID = "retail_demand_raw"

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


# M5 files and their BigQuery table names
FILES_TO_LOAD = {
    "calendar.csv": "calendar",
    "sales_train_validation.csv": "sales_train_validation",
    "sell_prices.csv": "sell_prices",
}


def load_csv_to_bigquery(file_name, table_name):
    """Load one CSV file from data/raw into BigQuery."""

    file_path = RAW_DATA_DIR / file_name
    table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    client = bigquery.Client(project=PROJECT_ID)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        allow_quoted_newlines=True,
    )

    print(f"\nLoading {file_name}...")
    print(f"Destination: {table_id}")

    with open(file_path, "rb") as file:
        load_job = client.load_table_from_file(
            file,
            table_id,
            job_config=job_config,
        )

    load_job.result()

    table = client.get_table(table_id)

    print(f"Successfully loaded: {table_id}")
    print(f"Rows: {table.num_rows}")
    print(f"Columns: {len(table.schema)}")


def main():
    print("M5 Dataset → BigQuery ETL")
    print("=" * 40)

    for file_name, table_name in FILES_TO_LOAD.items():
        load_csv_to_bigquery(file_name, table_name)

    print("\nAll M5 files loaded successfully!")


if __name__ == "__main__":
    main()