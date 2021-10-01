from datetime import timedelta
from airflow import DAG
import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from spotify_etl import run_spotify_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.datetime(2021, 10, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
        dag_id='spotify_dag',
        default_args=default_args,
        description='ETL',
        schedule_interval=timedelta(days=1),
    ) as f:

    run_etl = PythonOperator(
        task_id='whole_spotify_etl',
        python_callable=run_spotify_etl
    )

run_etl
