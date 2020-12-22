"""
This module restores an env from json and runs it.
"""
import importlib

from lib.model import Model
from APIServer.models_api import get_model


def create_model(model_id, props, indra_dir):
    """
    We get some props and create a model in response.
    """
    model = get_model(model_id, indra_dir=indra_dir)
    mod_name = f'{model["package"]}.{model["module"]}'
    print("mod_name = ", mod_name)
    this_mod = importlib.import_module(mod_name)
    model = this_mod.create_model()
    return model


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
