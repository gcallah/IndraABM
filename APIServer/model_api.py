"""
This module restores an env from json and runs it.
"""
import importlib

from registry.model_db import get_model_by_id, get_model_by_mod
from APIServer.api_utils import err_return


def module_from_model(model):
    mod_path = f'{model["package"]}.{model["module"]}'
    return importlib.import_module(mod_path)


def create_model(model_id, props, indra_dir):
    """
    We get some props and create a model in response.
    """
    model_rec = get_model_by_id(model_id, indra_dir=indra_dir)
    if model_rec is not None:
        return module_from_model(model_rec).create_model(props=props)
    else:
        return err_return("Model not found: " + str(model_id))


def run_model(serial_model, periods, indra_dir):
    """
    We get passed `serial_model` and run it `periods` times.
    `model_rec` refers to the record from the model db.
    `model` refers to an instance of the Python Model class.
    """
    model_rec = get_model_by_mod(serial_model["module"], indra_dir=indra_dir)
    if model_rec is not None:
        module = module_from_model(model_rec)
        model = module.create_model(serial_obj=serial_model)
        model.runN(periods)
        return model
    else:
        return None
