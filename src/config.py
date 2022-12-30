import os
import json


def load(file: str) -> dict[str, str]:
    if not os.path.exists(file):
        raise FileNotFoundError(f"File {file} does not exist")

    with open(file, "r") as f:
        return json.load(f)
    