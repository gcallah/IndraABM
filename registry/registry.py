"""
This module registers agent objects by name in a dictionary,
where the value should be the actual agent object. Since groups
and environments are agents, they should be registered here as
well.
While this is (right now) a simple dictionary, providing this
interface means that in the future, we can have something fancier,
if need be.
For instance, we might turn the registry into an object, but so long
as these functions still work, and no code goes straight at the dict,
that should break nothing.
We will add to the dict a check that what is being registered is an
agent!
IMPORTANT: Given our registry structure, *every agent name must be unique in a
run of a model*!
"""
import numpy as np
from numpy import random
import os
from os import listdir
from os.path import isfile, join
import json
import types

from lib.agent import Agent
from lib.env import Env

DEBUG = False

BILLION = 10 ** 9

EXEC_KEY = "exec_key"

ENV_NM = 'env'
MODEL_NM = 'model'

registry = None


def create_exec_env():
    return registry.create_exec_env()


def get_exec_key(**kwargs):
    exec_key = kwargs.get(EXEC_KEY, None)
    if exec_key is None:
        raise ValueError("Cannot find exec key:", exec_key)
    return exec_key


def get_model(exec_key):
    return get_agent(MODEL_NM, exec_key)


def get_env(exec_key=None, **kwargs):
    """
    :param execution_key: execution to fetch with
    :return: Env object
    """
    if exec_key is None:
        exec_key = get_exec_key(**kwargs)
    return get_agent(ENV_NM, exec_key)


def reg_model(model, exec_key):
    registry[exec_key][MODEL_NM] = model


def reg_agent(name, agent, exec_key):
    """
    Register an agent in the registry.
    Raises an exception if `agent` is not an `Agent`.
    Return: None
    """
    if not isinstance(name, str):
        raise ValueError("Key being registered is not a string.")
    if not isinstance(agent, Agent):
        raise ValueError("Object being registered is not an agent.")
    if len(name) == 0:
        raise ValueError("Cannot register agent with empty name")
    if isinstance(agent, Env):
        name = ENV_NM
    if exec_key is None:
        raise ValueError("Cannot register agent against a None Key")
    registry[exec_key][name] = agent


def get_agent(name, exec_key=None, **kwargs):
    """
    Fetch an agent from the registry.
    Return: The agent object.
    """
    if exec_key is None:
        exec_key = get_exec_key(**kwargs)
    if len(name) == 0:
        raise ValueError("Cannot fetch agent with empty name")
    if name in registry[exec_key]:
        return registry[exec_key][name]
    else:
        return None


def del_agent(name, exec_key=None, **kwargs):
    """
    Delete an agent from the registry.
    Return: None
    """
    if exec_key is None:
        exec_key = get_exec_key(**kwargs)
    del registry[exec_key][name]


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
    There might be optimizations here later.
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
                try:
                    if int(file.split("-")[0]) == key:
                        self.load_reg(key)
                        return True
                except ValueError:
                    # ignore files that don't start with an int!
                    pass
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
        print(f'Saving registry to disk {key}-reg.json')
        file_path = self.__get_reg_file_name(key)
        serial_object = json.dumps(self[key], cls=AgentEncoder,
                                   indent=4)
        with open(file_path, 'w') as file:
            file.write(serial_object)

    def load_reg(self, key):
        file_path = self.__get_reg_file_name(key)
        with open(file_path, 'r') as file:
            registry_as_str = file.read()

        return self.__json_to_object(json.loads(registry_as_str), key)

    '''
    restores the json object to python object
    '''

    def __json_to_object(self, serial_obj, exec_key):
        restored_obj = dict()
        restored_groups = []
        model_deserialized = False
        for obj_name in serial_obj:
            should_restore_object = isinstance(serial_obj[obj_name],
                                               dict) and "type" in serial_obj[
                                        obj_name]
            if should_restore_object:
                if serial_obj[obj_name]["type"] == "Agent":
                    restored_obj[obj_name] = Agent(name=obj_name,
                                                   serial_obj=serial_obj[
                                                       obj_name],
                                                   exec_key=exec_key)
                elif serial_obj[obj_name]["type"] == "Model":
                    from lib.model import Model
                    restored_obj[obj_name] = Model(exec_key=exec_key,
                                                   serial_obj=serial_obj[
                                                       obj_name])
                    model_deserialized = True
                elif serial_obj[obj_name]["type"] == "Group":
                    from lib.group import Group
                    restored_obj[obj_name] = Group(exec_key=exec_key,
                                                   serial_obj=serial_obj[
                                                       obj_name],
                                                   name=serial_obj[obj_name][
                                                       'name'])
                    restored_groups.append(restored_obj[obj_name])
            else:
                restored_obj[obj_name] = serial_obj[obj_name]

        if model_deserialized:
            restored_obj['model'].groups = restored_groups
        return restored_obj

    def create_exec_env(self, save_on_register=True):
        """
        Create a new execution environment and return its key.
        """
        key = self.__get_unique_key()
        print("Creating new registry with key: {}".format(key))
        self.registries[key] = {}
        self.registries[key] = {'save_on_register': save_on_register}
        # stores the file paths of pickled functions
        self.registries[key]['functions']: {str: str} = {}
        return key

    def del_exec_env(self, key):
        """
        Remove an execution environment from the registry.
        """
        self.__does_key_exists(key)
        if DEBUG:
            print("Clearing exec env {} from registry".format(key))
        del self[key]


registry = Registry()
