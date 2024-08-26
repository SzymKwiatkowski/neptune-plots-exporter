"""Module providing helpers for simple functionalities not related to bussiness logic"""
from pathlib import Path
import json


def load_json(path: Path) -> dict:
    """
    :param path: path to json file
    :rtype: dictionary parsed from json
    """
    with open(path, 'r', encoding="utf-8") as file:
        data = json.load(file)

    return data
