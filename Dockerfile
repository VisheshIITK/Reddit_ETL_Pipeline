FROM apache/airflow:2.10.4

COPY requirements.txt /opt/airflow/

# USER root
# RUN apt-get update && apt-get install -y gcc python3-dev

# USER airflow

# RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /opt/airflow/requirements.txt