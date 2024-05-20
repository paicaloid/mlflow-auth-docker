import os

from mlflow.server.auth.client import AuthServiceClient

client = AuthServiceClient(os.environ["MLFLOW_TRACKING_URI"])


client.update_user_password(
    username=os.environ["MLFLOW_TRACKING_USERNAME"],
    password=os.environ["MLFLOW_TRACKING_NEW_PASSWORD"],
)
