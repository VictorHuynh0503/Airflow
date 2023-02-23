import datetime as dt
from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd 
import request

default_args= {
    "owner":"vihuynh",
    "start_date":dt.datetime(2023, 2, 23),
    "retries":1,
    "retry_delay": dt.timedelta(minutes=5)
}

def call_api_to_webhook():
    url = "https://webhook.site/3a9af45f-fbb1-4da1-b5f5-885d9466c0d6"
    request = requests.get(url)
    return request

with DAG(
    "test_new_vi",
    default_args=default_args,
    schedule_interval="* */1 * * *"
) as dag:

    python_task = PythonOperator(
    task_id="python_task",
    python_callable=call_api_to_webhook(),
    # op_kwargs: Optional[Dict] = None,
    # op_args: Optional[List] = None,
    # templates_dict: Optional[Dict] = None
    # templates_exts: Optional[List] = None
    )


    bash_task = BashOperator(
    task_id="bash_task",
    bash_command='echo "Call webhook to test"',
    # env: Optional[Dict[str, str]] = None,
    # output_encoding: str = 'utf-8',
    # skip_exit_code: int = 99,
    )

    python_task >> bash_task