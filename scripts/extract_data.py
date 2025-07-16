import requests
import json
from datetime import datetime, timedelta
import os
from google.cloud import storage
from dotenv import load_dotenv

load_dotenv()

# === CONFIGURAÇÕES ===
API_KEY = os.getenv("OPENAQ_API_KEY")
SENSOR_ID = 23534
START_DATE = "2024-01-01"
END_DATE = "2024-12-31"
BUCKET_NAME = "etl-air-quality-raw-data-project"  
GCS_PATH = f"raw/openaq_daily_{SENSOR_ID}.json"
LOCAL_PATH = f"data/raw/openaq_daily_{SENSOR_ID}.json"

headers = {
    "X-API-Key": API_KEY
}

def fetch_daily_data(sensor_id, date_from, date_to):
    url = f"https://api.openaq.org/v3/sensors/{sensor_id}/days"
    params = {
        "date_from": date_from,
        "date_to": date_to,
        "limit": 1000,  # limite máximo
        "page": 1
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def save_local(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Dados salvos localmente em {path}")

def upload_to_gcs(local_file, bucket_name, gcs_path):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(gcs_path)
    blob.upload_from_filename(local_file)
    print(f"Arquivo enviado para gs://{bucket_name}/{gcs_path}")

def main():
    print("🔄 Baixando dados diários...")
    data = fetch_daily_data(SENSOR_ID, START_DATE, END_DATE)

    print("💾 Salvando localmente...")
    os.makedirs("data/raw", exist_ok=True)
    save_local(data, LOCAL_PATH)

    print("☁️ Enviando para o Google Cloud Storage...")
    upload_to_gcs(LOCAL_PATH, BUCKET_NAME, GCS_PATH)

if __name__ == "__main__":
    main()