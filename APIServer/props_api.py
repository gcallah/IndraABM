import json

from lib.utils import get_prop_path
from APIServer.api_utils import json_converter, err_return
from APIServer.models_api import get_model
from registry.registry import get_env

ENV_INSTANCE = 0


def get_props_for_curr_exec(model_id, indra_dir):
    try:
        # execution_key = Registry.create_exec_env()
        model = get_model(model_id, indra_dir=indra_dir)
        prop_file = get_prop_path(model["module"], model["package"])
        print("prop_file = ", prop_file)
        with open(prop_file) as file:
            props = json.loads(file.read())
        return props
    except (IndexError, KeyError, ValueError):
        return err_return("Invalid model id " + str(model_id))
    except FileNotFoundError:  # noqa: F821
        return err_return("Models or props file not found")


# The execution environment doesn't seem to have been created, excution key is
# correct but the call to get_env returns none
def put_props(model_id, payload, indra_dir):
    print(payload)
    exec_key = payload["execution_key"].get("val")
    print("The execution key in put props is", exec_key)
    # the exec env is currently none
    print("The execution environment is", get_env(exec_key=exec_key))
    return json_converter(
        get_env(exec_key=exec_key), execution_key=exec_key)
