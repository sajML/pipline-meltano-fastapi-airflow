# Astro CLI (Airflow) Project for viceversa exercise 1
========

Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.

Project Contents
================

Your Astro project contains the following files and folders:

 dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes one example DAG:

 - `pipe.py`: This DAG demonstrates a simple ETL pipeline that retrieves data from a dummy API and loads it into a CSV file using Meltano. It then uses FastAPI to fetch data from the CSV file and replace NaN values with None. The DAG uses the TaskFlow API to define tasks in Python, and dynamic task mapping to orchestrate the pipeline. For more on how this DAG works, see the code in the pipe.py file. 

- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

## Usage
### Deploy Your Project Locally

1. Start Airflow and create csv file on your local machine (`for windows C:\output`) by running:
```bash
# Clone project
git clone https://github.com/sajML/pipline-meltano-fastapi-airflow.git
cd pipline-meltano-fastapi-airflow
astro dev start
```

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://docs.astronomer.io/astro/test-and-troubleshoot-locally#ports-are-not-available).

3. Access the Airflow UI for your local Airflow project. To do so, go to `http://localhost:8080/` and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.

