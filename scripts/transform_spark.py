from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp
import json
import os

RAW_JSON_PATH = "data/raw/openaq_daily_23534.json"
PARQUET_OUTPUT_PATH = "data/parquet/openaq_daily_23534.parquet"

def main():
    # Cria sessão Spark
    spark = SparkSession.builder \
        .appName("Transform OpenAQ JSON") \
        .getOrCreate()

    # Carrega JSON bruto
    with open(RAW_JSON_PATH) as f:
        data = json.load(f)

    records = data.get("results", [])
    if not records:
        raise ValueError("Nenhum dado encontrado em 'results'")

    # Cria DataFrame Spark
    df = spark.read.json(spark.sparkContext.parallelize([json.dumps(r) for r in records]))

    # Seleciona e renomeia colunas (igual pandas)
    selected_df = df.select(
        col("value"),
        col("parameter.name").alias("parameter_name"),
        col("parameter.units").alias("units"),
        col("period.datetimeFrom.utc").alias("datetime_from"),
        col("period.datetimeTo.utc").alias("datetime_to"),
        col("summary.min").alias("summary_min"),
        col("summary.max").alias("summary_max"),
        col("summary.avg").alias("summary_avg"),
        col("summary.sd").alias("summary_sd"),
        col("coverage.percentComplete").alias("coverage_percent_complete")
    )

    # Conversão de datas
    selected_df = selected_df.withColumn("datetime_from", to_timestamp("datetime_from")) \
                             .withColumn("datetime_to", to_timestamp("datetime_to"))

    # Remove linhas com valor nulo
    cleaned_df = selected_df.dropna(subset=["value"])

    # Salva como Parquet
    cleaned_df.write.mode("overwrite").parquet(PARQUET_OUTPUT_PATH)

    print(f"✅ Dados transformados e salvos como Parquet em {PARQUET_OUTPUT_PATH}")
    spark.stop()

if __name__ == "__main__":
    main()
