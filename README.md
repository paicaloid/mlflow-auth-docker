# MLflow Deployment using Docker Compose with Authentication
MLflow Server with [Authentication](https://mlflow.org/docs/latest/auth/index.html)

This is an update version from [Toumash/mlflow-docker](https://github.com/Toumash/mlflow-docker)

## Update
 - Add reverse proxy for MinIO and MLflow

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

## Reverse Proxy with Nginx
1. [How To Install Nginx on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04) with [server blocks](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04#step-5-setting-up-server-blocks-recommended)
2. [How To Secure Nginx with Let's Encrypt on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04)
3. Configuration for Nginx `/etc/nginx/sites-available/__servername__` from `nginx.conf` refer to [Configure NGINX Proxy for MinIO Server](https://min.io/docs/minio/linux/integrations/setup-nginx-proxy-with-minio.html)
4. Chagne `DOMAIN` in `.env` to your domain
5. Run `docker-compose up -d`
6. Access MinIO GUI at `https://DOMAIN/minio/ui/` with `MINIO_ROOT_USER` and `MINIO_ROOT_PASSWORD`
7. Access MLflow at `https://DOMAIN/mlflow/` with `MLFLOW_TRACKING_USERNAME` and `MLFLOW_TRACKING_NEW_PASSWORD`

## Note
- For Authentication, this feature is available in MLflow version 2.13.0 but this feature is still experimental and may change in a future release without warning.