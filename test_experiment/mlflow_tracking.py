import os
from pathlib import Path
from random import randint, random

import mlflow

if __name__ == "__main__":
    mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
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
