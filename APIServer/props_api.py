import json

from APIServer.api_utils import json_converter, err_return
from APIServer.models_api import get_model
from registry.registry import EXEC_KEY
from registry.registry import get_env

ENV_INSTANCE = 0


def get_props_for_current_execution(model_id, indra_dir):
    try:
        # execution_key = Registry.create_exec_env()
        model = get_model(model_id, indra_dir=indra_dir)
        with open(indra_dir + "/" + model["props"]) as file:
            props = json.loads(file.read())
        # Registry.set_propargs(execution_key, props)
        # props[EXEC_KEY] = \
            # Registry.get_execution_key_as_prop(execution_key)
        return props
    except (IndexError, KeyError, ValueError):
        return err_return("Invalid model id " + str(model_id))
    except FileNotFoundError:  # noqa: F821
        return err_return("Models or props file not found")


def put_props(model_id, payload, indra_dir):
    execution_key = payload[EXEC_KEY].get("val")
    # model = get_model(model_id, indra_dir=indra_dir)
    return json_converter(
        get_env(execution_key=execution_key), execution_key=execution_key)
