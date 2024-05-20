# MLflow Deployment using Docker Compose with Authentication
MLflow Server with [Authentication](https://mlflow.org/docs/latest/auth/index.html)

This is an update version from [Toumash/mlflow-docker](https://github.com/Toumash/mlflow-docker)
## Features
  - MLflow server
  - MinIO GUI as artifact storage
  - PostgreSQL as mlflow storage
  - scripts to create user and assign policy for MinIO
  - scripts to creaet s3 bucket
  - automated update password for MLflow admin
  - test log experiment to MLflow

## Setup
1. Change parameter in `.env`, expetially for password and secret key
   -  `POSTGRES_USER`, `POSTGRES_PASSWORD` for PostgreSQL
   -  `MINIO_ROOT_USER` and `MINIO_ROOT_PASSWORD` for MinIO ROOT user
   -  `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for MinIO user to access S3 bucket from MLflow
   -  `MLFLOW_TRACKING_USERNAME` and `MLFLOW_TRACKING_PASSWORD` for MLflow admin, initial from MLflow Authentication
   -  `MLFLOW_TRACKING_NEW_PASSWORD` update password for MLflow admin
2. Run `docker-compose up -d`
3. Access MinIO GUI at [http://localhost:9000](http://localhost:9000) with `MINIO_ROOT_USER` and `MINIO_ROOT_PASSWORD`
4. Access MLflow at [http://localhost:5000]([http://localhost:5000) with `MLFLOW_TRACKING_USERNAME` and `MLFLOW_TRACKING_NEW_PASSWORD`

## Note
- For Authentication, this feature is available in MLflow version 2.13.0 but this feature is still experimental and may change in a future release without warning.