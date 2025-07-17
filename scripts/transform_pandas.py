import json
import pandas as pd
import os

BASE_DIR = os.environ.get("DATA_PATH", os.path.abspath("."))
RAW_JSON_PATH = os.path.join(BASE_DIR, "data", "raw", "openaq_daily_23534.json")
PROCESSED_CSV_PATH = os.path.join(BASE_DIR, "data", "processed", "openaq_daily_23534_processed.csv")

def load_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data

def transform_data(data):
    # Extrai lista de resultados
    results = data.get("results", [])
    if not results:
        raise ValueError("Nenhum dado encontrado na chave 'results'")

    # Cria DataFrame
    df = pd.json_normalize(results)

    # Seleciona colunas relevantes (exemplo baseado na sua lista)
    cols = [
        'value',
        'parameter.name',
        'parameter.units',
        'period.datetimeFrom.utc',
        'period.datetimeTo.utc',
        'summary.min',
        'summary.max',
        'summary.avg',
        'summary.sd',
        'coverage.percentComplete'
    ]
    df = df[cols]

    # Renomeia colunas para mais simples
    df.columns = [
        'value',
        'parameter_name',
        'units',
        'datetime_from',
        'datetime_to',
        'summary_min',
        'summary_max',
        'summary_avg',
        'summary_sd',
        'coverage_percent_complete'
    ]

    # Conversão de datas
    df['datetime_from'] = pd.to_datetime(df['datetime_from'])
    df['datetime_to'] = pd.to_datetime(df['datetime_to'])

    # Tratamento de nulos (exemplo: remover linhas com valor nulo)
    df = df.dropna(subset=['value'])

    return df

def save_csv(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"CSV processado salvo em {path}")

def main():
    print("📥 Carregando dados JSON...")
    data = load_json(RAW_JSON_PATH)

    print("⚙️ Transformando dados com pandas...")
    df = transform_data(data)

    print("📤 Salvando CSV processado...")
    save_csv(df, PROCESSED_CSV_PATH)

    print("✅ Transformação finalizada!")

if __name__ == "__main__":
    main()