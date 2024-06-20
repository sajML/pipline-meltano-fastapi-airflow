from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount
import os


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'meltano_fastapi_dag',
    default_args=default_args,
    description='A simple DAG to run Meltano and then FastAPI',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:
    
    host = 'host.docker.internal' # If you are running airflow from docker
        # Otherwise host = 'localhost'
    current_directory = os.getcwd() # Get the current directory

    run_meltano = DockerOperator(
        task_id='run_meltano',
        image='sajjadgoudarzi/vicev-ex1-meltano:latest',
        api_version='auto',
        auto_remove=True,
        command="run tap-ex1 target-csv",
        docker_url=f'tcp://{host}:2375',
        network_mode='bridge',
        mounts=[
            Mount(
                source= "C:\\output", 
                target='/app/output', 
                type='bind'
            )
        ],
        #working_dir= '/app'
    )

    run_fastapi = DockerOperator(
        task_id='run_fastapi',
        image='sajjadgoudarzi/vicev-ex1-fastapi:v1',
        api_version='auto',
        auto_remove=True,
        command="uvicorn run_api:app --host 0.0.0.0 --port 8000",
        docker_url=f'tcp://{host}:2375',
        network_mode='bridge',
        mounts=[
            Mount(
                source= "C:\\output", 
                target='/app/output', 
                type='bind'
            )
        ],        
        port_bindings = {8000:8001}
    )

    run_meltano >> run_fastapi
