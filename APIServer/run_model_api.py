"""
This module restores an env from json and runs it.
"""
from APIServer.api_utils import json_converter
from lib.model import Model


def run_model_put(payload, run_time):
    """
    We create a dummy env that fills itself in to create
    the real env from the payload.
    """
    execution_key = payload.get("exec_key")
    print("Got execution key", execution_key)
    model = Model("test_model")
    return json_converter(model)
