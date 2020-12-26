# This module handles the models portion of the API server.

import json
from APIServer.api_utils import ERROR

REGISTRY = "registry"
MODELS_DB = "models.json"
MODEL_FILE = "/" + REGISTRY + "/" + MODELS_DB
MODEL_ID = "model ID"
MODEL_MOD = "module"


def load_models(indra_dir):
    """
    Load models database into memory.
    """
    model_file = indra_dir + MODEL_FILE
    try:
        with open(model_file) as file:
            return json.loads(file.read())["models_database"]
    except FileNotFoundError:  # noqa: F821
        return None


def get_models(indra_dir):
    """
    Return the models database as a list of models.
    """
    models_db = load_models(indra_dir)
    if models_db is None:
        return {ERROR: "Model file not found: indra dir is " + indra_dir}

    models_response = []
    for model in models_db:
        models_response.append(model)
    return models_response


def get_model_by_id(model_id, indra_dir=''):
    """
    Fetch a model from the model db by id.
    """
    models_db = load_models(indra_dir)
    if models_db is None:
        return None
    for model in models_db:
        if int(model[MODEL_ID]) == model_id:
            return model
    return None


def get_model_by_mod(mod, indra_dir=''):
    """
    Fetch a model from the model db by module name.
    """
    models_db = load_models(indra_dir)
    if models_db is None:
        return None
    for model in models_db:
        if model[MODEL_MOD] == mod:
            return model
    return None
