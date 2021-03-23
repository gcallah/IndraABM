import os
import platform

from propargs.constants import OS, ENV_AUTO_LOAD_PROPS


def set_props_from_env(prop_args):
    _set_auto_load_props(prop_args)
    _overwrite_existing_props(prop_args)

def _set_auto_load_props(prop_args):
    for prop_name, default in ENV_AUTO_LOAD_PROPS:
        prop_args[prop_name] = os.environ.get(prop_name, default=default)

def _overwrite_existing_props(prop_args):
    env_dict = os.environ
    common_prop_keys = env_dict.keys() & prop_args.props.keys()
    for key in common_prop_keys:
        prop_args[key] = env_dict[key]

    prop_args[OS] = platform.system()
