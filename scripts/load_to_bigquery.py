from google.cloud import bigquery
import pandas as pd
import os

# Caminhos
PARQUET_PATH = "data/parquet/openaq_daily_23534.parquet"
GCP_PROJECT = "etl-air-quality-project" 
DATASET_ID = "air_quality"
TABLE_ID = "daily_measurements"

def main():
    print("📥 Lendo Parquet com pandas...")
    df = pd.read_parquet(PARQUET_PATH)

    print("☁️ Conectando ao BigQuery...")
    client = bigquery.Client(project=GCP_PROJECT)

    table_ref = f"{GCP_PROJECT}.{DATASET_ID}.{TABLE_ID}"

    print(f"⬆️ Enviando dados para {table_ref}...")

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",  # sobrescreve se já existir
        source_format=bigquery.SourceFormat.PARQUET,
        autodetect=True,
    )

    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()  # Espera o job finalizar

    print("✅ Dados carregados com sucesso no BigQuery!")

if __name__ == "__main__":
    main()
