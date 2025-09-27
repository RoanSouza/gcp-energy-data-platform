from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

def ingest_data():
    data = {
        "data": pd.date_range("2021-01-01", periods=5, freq="M"),
        "consumo_mwh": [1000, 1200, 1100, 1500, 1700],
        "cidade": ["Rio", "SP", "BH", "Curitiba", "Fortaleza"]
    }
    df = pd.DataFrame(data)
    df.to_csv("/tmp/energy_data_raw.csv", index=False)

def transform_data():
    df = pd.read_csv("/tmp/energy_data_raw.csv")
    df["consumo_kwh"] = df["consumo_mwh"] * 1000
    df.to_csv("/tmp/energy_data_refined.csv", index=False)

default_args = {
    "owner": "roan",
    "start_date": datetime(2025, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="energy_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    task_ingest = PythonOperator(
        task_id="ingest_data",
        python_callable=ingest_data
    )

    task_transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    task_ingest >> task_transform
