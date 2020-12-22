"""
This module restores an env from json and runs it.
"""
from lib.model import Model
from APIServer.models_api import get_model
from models.basic import basic_create_model # noqa F401
from models.forest_fire import forest_fire_create_model # noqa F401
from models.el_farol import el_farol_create_model # noqa F401
from models.panic import panic_create_model # noqa F401
from models.game_of_life import game_of_life_create_model # noqa F401


def create_model(model_id, props, indra_dir):
    """
    We get some props and create a model in response.
    """
    model = get_model(model_id, indra_dir=indra_dir)
    create_model_func = model["create_model"]
    print("The create model func is", create_model_func)
    model = eval(create_model_func)
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
