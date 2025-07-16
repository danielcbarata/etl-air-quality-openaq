# ETL Air Quality - OpenAQ

ETL pipeline for air quality analysis with OpenAQ data, using PySpark, pandas, GCP and visualization with Plotly.

## 🔧 Tools and Technologies

- Python
- PySpark
- pandas
- Google Cloud Platform (GCS + BigQuery)
- Plotly

## 📁 Project Structure
```
etl-air-quality-openaq/
├── data/
│ ├── raw/
│ └── parquet/
│ └── processed/
├── scripts/
├── visualizations/
├── requirements.txt
└── README.md
```
## 📌 Steps

1. Data Extraction
2. Transformation (Spark & pandas)
3. Load to BigQuery
4. Analysis & Visualization

## Visualizations

Interactive Plotly graphs are generated and saved as `.html` files in the `visualizations/` folder.

To view the charts, please download the `.html` file and open it with your web browser, as GitHub does not render HTML files directly.