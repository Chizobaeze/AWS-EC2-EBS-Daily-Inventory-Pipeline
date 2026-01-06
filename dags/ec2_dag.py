from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from dags.ec2_extract import ec2_data

default_args = {
    'owner': 'chizoba',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 2,
}

with DAG(
    dag_id="chizoba_ec2_inventory_to_s3",
    default_args=default_args,        
    schedule_interval="@daily",       
    catchup=False,      
) as dag:

    extract_ec2_task = PythonOperator(
        task_id="extract_ec2_data",
        python_callable=ec2_data
    )
