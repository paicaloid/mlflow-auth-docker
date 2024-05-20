FROM ghcr.io/mlflow/mlflow:v2.13.0

RUN pip install -U psycopg2-binary boto3 mlflow