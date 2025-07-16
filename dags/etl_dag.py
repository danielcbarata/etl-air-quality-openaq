from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'daniel',
    'start_date': days_ago(1),
}

with DAG(
    'etl_air_quality',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['etl', 'openaq'],
) as dag:

    extract = BashOperator(
        task_id='extract_data',
        bash_command='python /opt/airflow/scripts/extract_data.py',
    )

    transform_pandas = BashOperator(
        task_id='transform_pandas',
        bash_command='python /opt/airflow/scripts/transform_pandas.py',
    )

    transform_spark = BashOperator(
        task_id='transform_spark',
        bash_command='python /opt/airflow/scripts/transform_spark.py',
    )

    load_bq = BashOperator(
        task_id='load_bigquery',
        bash_command='python /opt/airflow/scripts/load_to_bigquery.py',
    )

    visualize = BashOperator(
        task_id='visualize_plotly',
        bash_command='python /opt/airflow/visualizations/bq_plotly.py',
    )

    extract >> transform_pandas >> transform_spark >> load_bq >> visualize
