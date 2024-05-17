FROM ghcr.io/mlflow/mlflow

RUN pip install -U psycopg2-binary boto3 mlflow