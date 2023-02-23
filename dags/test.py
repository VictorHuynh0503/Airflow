import datetime as dt
from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd 


default_args= {
    "owner":"vihuynh",
    "start_date":dt.datetime(2023, 2, 10),
    "retries":1,
    "retry_delay": dt.timedelta(minutes=5)
}

with DAG(
    "test_new_vi",
    default_args=default_args,
    schedule_interval="* */1 * * *"
) as dag:

    python_task = PythonOperator(
    task_id="python_task",
    python_callable=lambda: print('Hi from python operator'),
    # op_kwargs: Optional[Dict] = None,
    # op_args: Optional[List] = None,
    # templates_dict: Optional[Dict] = None
    # templates_exts: Optional[List] = None
    )


    bash_task = BashOperator(
    task_id="bash_task",
    bash_command='echo "Hi from bash operator"',
    # env: Optional[Dict[str, str]] = None,
    # output_encoding: str = 'utf-8',
    # skip_exit_code: int = 99,
    )

    python_task >> bash_task