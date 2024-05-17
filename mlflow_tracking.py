import os
from pathlib import Path
from random import randint, random

import mlflow

os.environ["MLFLOW_TRACKING_USERNAME"] = "admin"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "password"


os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:9000"
os.environ["AWS_ACCESS_KEY_ID"] = "sample"
os.environ["AWS_SECRET_ACCESS_KEY"] = "samplekey"

if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:5000/")
    mlflow.start_run()

    mlflow.log_param("param1", randint(0, 100))

    mlflow.log_metric("foo", random())
    mlflow.log_metric("foo", random() + 1)
    mlflow.log_metric("foo", random() + 2)

    if not Path("outputs").exists():
        Path("outputs").mkdir(parents=True, exist_ok=True)

    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")

    mlflow.log_artifacts("outputs")

    mlflow.end_run()
