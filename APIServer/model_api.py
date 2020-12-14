"""
This module restores an env from json and runs it.
"""
from lib.model import Model


def create_model(model_id, props, indra_dir):
    """
    We get some props and create a model in response.
    """
    return Model("test_model", props=props)


def run_model(serial_model, run_time):
    """
    We create a dummy env that fills itself in to create
    the real env from the payload.
    """
    print("About to recreate model from json")
    model = Model(serial_obj=serial_model)
    print("About to run model restored from json")
    model.runN(run_time)
    return model
