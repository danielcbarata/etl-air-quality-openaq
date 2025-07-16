# ETL Air Quality - OpenAQ

ETL pipeline for air quality analysis with OpenAQ data, using PySpark, pandas, GCP, Docker, Airflow and visualization with Plotly.

## ✅ Features

* Data extraction via OpenAQ API
* Local storage (raw JSON + Parquet)
* Upload to Google Cloud Storage
* Transformation with pandas and PySpark
* Load to Google BigQuery
* Visualization with Plotly
* Orchestration with Apache Airflow
* Containerization with Docker

## 🔧 Tools and Technologies

* Python
* PySpark
* pandas
* Google Cloud Storage
* Google BigQuery
* Apache Airflow
* Docker
* Plotly

## 📁 Project Structure

```
etl-air-quality-openaq/
├── data/
│   ├── raw/          # Raw JSON data
│   ├── parquet/      # Converted Parquet files
│   └── processed/    # Cleaned/processed datasets
├── dags/
│   └── etl_dag.py    # Airflow DAG definition
├── scripts/          # ETL scripts
│   ├── extract_data.py
│   ├── load_to_bigquery.py
│   ├── transform_pandas.py
│   ├── transform_spark.py
│   └── .env.example  # Example of OpenAQ API key
├── visualizations/   # Plotly HTML files
│   ├── bq_plotly.py
│   └── pm25_avg.html
├── .env.example      # Example with Airflow secrets (FERNET_KEY)
├── docker-compose.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

## 📌 Steps

1. Data Extraction (OpenAQ API)
2. Transformation (pandas & PySpark)
3. Load to BigQuery
4. Visualization using Plotly

## 🔐 Environment Variables

This project uses two `.env.example` files:

* `scripts/.env.example`:

  * `OPENAQ_API_KEY=your_openaq_api_key_here`
* `.env.example` (root directory):

  * `FERNET_KEY=your_fernet_key_here` (used by Airflow for encryption)

Rename and edit them to `.env` before running locally or in Docker.

## 📊 Visualizations

The interactive Plotly graph is saved as an HTML file in the `visualizations/` folder.

**To view the graph:**

* Download the `visualizations/pm25_avg.html` file to your local machine.
* Open it with any modern web browser (Chrome, Firefox, Edge, etc.).
* The graph is fully interactive with zoom, pan, and tooltips.

> Note: GitHub does not render HTML files directly in the browser for security reasons, so you must download it first.

## 🚀 Running the Project

You can run the pipeline either locally or using Docker.

### Option 1: Local Execution

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up `.env` files as needed
4. Run scripts manually in the desired order from the `scripts/` folder

### Option 2: Docker + Airflow

1. Ensure Docker and Docker Compose are installed
2. Start the containers:

```bash
docker-compose up --build
```

3. Access Airflow UI:

* URL: [http://localhost:8080](http://localhost:8080)
* Username: `admin` — Password: `admin`

4. Trigger the DAG `etl_air_quality` from the web interface

## 📌 Highlights

* Full ETL pipeline using real-world tools
* Scalable transformation with PySpark
* Integration with Google Cloud Storage & BigQuery
* Dockerized + orchestrated with Apache Airflow
* Interactive visualizations from BigQuery results

## 🪪 License

This project is licensed under the [MIT License](LICENSE).