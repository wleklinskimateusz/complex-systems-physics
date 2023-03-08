import os
from const import OUTPUT


def output_path(filename: str) -> str:
    return os.path.join(OUTPUT, filename)


def create_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)
