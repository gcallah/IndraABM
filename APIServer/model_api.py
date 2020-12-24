"""
This module restores an env from json and runs it.
"""
import importlib
from lib.model import Model
from APIServer.models_api import get_model, load_models


def create_model(model_id, props, indra_dir):
    """
    We get some props and create a model in response.
    """
    model = get_model(model_id, indra_dir=indra_dir)
    mod_name = f'{model["package"]}.{model["module"]}'
    this_mod = importlib.import_module(mod_name)
    model = this_mod.create_model()
    return model


def run_model(serial_model, run_time, indra_dir):
    """
    We create a dummy env that fills itself in to create
    the real env from the payload.
    """
    model_module = serial_model["name"]
    models_db = load_models(indra_dir)
    for model in models_db:
        if model["module"] == model_module:
            mod_file = f'{model["package"]}.{model["module"]}'
            this_mod = importlib.import_module(mod_file)
            model = this_mod.create_model(serial_obj=serial_model)
            model.runN(run_time)
            return model
    print(model_module + " " + "was not found, creating the default model")
    model = Model(serial_obj=serial_model)
    return model
