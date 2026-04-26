from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    "traffic_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    ingest = BashOperator(
        task_id="data_ingestion",
        bash_command="python scripts/data_ingestion.py"
    )

    clean = BashOperator(
        task_id="data_cleaning",
        bash_command="python scripts/data_cleaning.py"
    )

    transform = BashOperator(
        task_id="data_transform",
        bash_command="python scripts/data_transform.py"
    )

    ingest >> clean >> transform