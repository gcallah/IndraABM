"""
Methods the Data Store import process
"""
import json
import os

from propargs import property_dict
from propargs.constants import PROPS_DIR


def set_props_from_ds(prop_args):
    if prop_args.ds_file:
        ds_dict = _open_file_as_json(prop_args.ds_file)
        property_dict.set_props_from_dict(prop_args, ds_dict)


def _open_file_as_json(ds_file):
    try:
        with open(_path_to_file(ds_file), 'r') as f:
            ds_dict = json.load(f)
    except FileNotFoundError:
        ds_dict = dict()
    return ds_dict


def _path_to_file(ds_file):
    if PROPS_DIR in os.environ:
        path = str(os.environ[PROPS_DIR])
    else:
        path = os.getcwd()

    return os.path.join(path, ds_file)
