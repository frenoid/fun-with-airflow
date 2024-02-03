import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="hello_world",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="*/5 * * * *",
    default_args={"retries": 2},
):
    hello_world = BashOperator(
        task_id="hello_world",
        bash_command="echo hello world!",
    )
