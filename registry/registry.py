import numpy as np
from numpy import random
import os
from os import listdir
from os.path import isfile, join
import json
import types
from propargs.constants import VALUE, ATYPE, INT, HIVAL, LOWVAL

from lib.agent import Agent

BILLION = 10 ** 9

EXEC_KEY = "execution_key"


def init_exec_key(props=None):
    if props is None:
        raise KeyError(
            "Cannot find key - {} in the passed props".format(EXEC_KEY))


def get_func_name(f):
    # Until Agent.restore and Env.to_json can restore functions from function
    # names, strings will be returned as-is.
    if isinstance(f, str):
        return f
    elif f is not None:
        return f.__name__
    else:
        return ""


class AgentEncoder(json.JSONEncoder):
    """
    The JSON encoder base class for all descendants
    of Agent.
    """

    def default(self, o):
        if hasattr(o, 'to_json'):
            return o.to_json()
        elif isinstance(o, np.int64):
            return int(o)
        elif isinstance(o, types.FunctionType):
            return get_func_name(o)  # can't JSON a function!
        else:
            return json.JSONEncoder.default(self, o)


class Registry(object):

    def __init__(self):
        print("Creating new registry")
        self.registries = dict()
        indra_dir = os.getenv("INDRA_HOME", "/home/IndraABM/IndraABM")
        self.db_dir = os.path.join(indra_dir, 'registry', 'db')
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

    '''
    set the item in the registry dictionary.
    if the flag save_on_register is set to true for
    agents stored against this key then save the
    registry to disk.
    NOTE: If save_on_register is set to false, the
    contents of registry wont be written to disk until someone
    calls save_reg with this key.
    '''
    def __setitem__(self, key, value):
        self.registries[key] = value
        if self.registries[key]['save_on_register']:
            self.save_reg(key)

    '''
    Always fetch the items from the file for now.
    There might be optimization's here later.
    '''
    def __getitem__(self, key):
        if key not in self:
            '''
            notice that this is only accessed by a thread that did not
            create this key.
            '''
            self.registries[key] = self.load_reg(key)
            return self.registries[key]

        return self.registries[key]

    '''
    Always check the files already written to the disk since
    some other thread might have stored a dictionary and the key
    will not be present here.
    NOTE: This might be a potential use for generators to lazy load
    the dictionary from file.
    '''
    def __contains__(self, key):
        if key in self.registries.keys():
            return True
        else:
            registry_files = [file for file in listdir(self.db_dir) if
                              isfile(join(self.db_dir, file))]
            for file in registry_files:
                if int(file.split("-")[0]) == key:
                    return True

            return False

    def __delitem__(self, key):
        del self.registries[key]

    def __get_unique_key(self):
        key = random.randint(1, BILLION)
        while key in self.registries.keys():
            key = random.randint(1, BILLION)
        return key

    def __get_reg_file_name(self, key):
        file_path = os.path.join(self.db_dir, '{}-reg.json'.format(key))
        return file_path

    def __does_key_exists(self, key):
        if key not in self:
            raise KeyError("Key - {} does not exist in registry.".format(key))
        return True

    def save_reg(self, key):
        file_path = self.__get_reg_file_name(key)
        serial_object = json.dumps(self[key], cls=AgentEncoder,
                                   indent=4)
        with open(file_path, 'w') as file:
            file.write(serial_object)

    def load_reg(self, key):
        file_path = self.__get_reg_file_name(key)
        with open(file_path, 'r') as file:
            registry_as_str = file.read()

        return self.__json_to_object(json.loads(registry_as_str))

    '''
    restores the json object to python object
    '''
    def __json_to_object(self, serial_obj):
        restored_obj = dict()
        for obj_name in serial_obj:
            should_restore_object = isinstance(serial_obj[obj_name],
                                               dict) and "type" in serial_obj[
                                        obj_name]
            if should_restore_object:
                if serial_obj[obj_name]["type"] == "Agent":
                    restored_obj[obj_name] = Agent(name=obj_name,
                                                   serial_obj=serial_obj[
                                                       obj_name])
            else:
                restored_obj[obj_name] = serial_obj[obj_name]
        return restored_obj

    def create_new_execution_registry(self, save_on_register=True):
        key = self.__get_unique_key()
        print("Creating new execution_registry with key-{}".format(key))
        self.registries[key] = {}
        self.registries[key] = {'save_on_register': save_on_register}
        return key

    def clear_registry(self, key):
        self.__does_key_exists(key)
        print("Clearing key - {} from registry".format(key))
        del self[key]


registry = Registry()
