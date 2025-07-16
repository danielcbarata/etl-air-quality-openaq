from google.cloud import bigquery
import pandas as pd
import plotly.express as px
import os

GCP_PROJECT = "etl-air-quality-project"
DATASET_ID = "air_quality"
TABLE_ID = "daily_measurements"

def fetch_data():
    client = bigquery.Client(project=GCP_PROJECT)
    query = f"""
        SELECT datetime_from, summary_avg
        FROM `{GCP_PROJECT}.{DATASET_ID}.{TABLE_ID}`
        ORDER BY datetime_from
        LIMIT 1000
    """
    df = client.query(query).to_dataframe()
    return df

def create_plot(df):
    fig = px.line(df, x="datetime_from", y="summary_avg",
                  title="Qualidade do Ar - Média Diária de PM2.5",
                  labels={"datetime_from": "Data", "summary_avg": "PM2.5 (µg/m³)"})
    return fig

def save_plot(fig, filename="visualizations/pm25_avg.html"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    fig.write_html(filename)
    print(f"Gráfico salvo em {filename}")

def main():
    print("♻️ Buscando dados do BigQuery...")
    df = fetch_data()

    print("📊 Criando gráfico com Plotly...")
    fig = create_plot(df)

    print("💾 Salvando gráfico em HTML...")
    save_plot(fig)

    print("✅ Visualização pronta!")

if __name__ == "__main__":
    main()
