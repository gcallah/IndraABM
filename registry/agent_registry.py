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
from lib.agent import Agent
from lib.env import Env
from registry.registry import registry

agent_reg = {}


def create_new_registry():
    return registry.create_new_execution_registry()


def get_env(execution_key):
    """
    :param execution_key: execution to fetch with
    :return: Env object
    """
    return get_agent('env', execution_key)


def reg_agent(name, agent, execution_key):
    """
    Register an agent in the registry.
    Raises an exception if `agent` is not an `Agent`.
    Return: None
    """
    if not isinstance(agent, Agent) or Agent is None:
        raise ValueError("Object being registered is not an agent.")
    if execution_key is None:
        raise ValueError("Cannot register agent without execution key")
    if len(name) == 0:
        raise ValueError("Cannot register agent with empty name")
    if isinstance(agent, Env):
        name = 'env'
    registry[execution_key][name] = agent


def get_agent(name, execution_key):
    """
    Fetch an agent from the registry.
    Return: The agent object.
    """
    if execution_key is None:
        raise ValueError("Cannot fetch agent without execution key")
    if len(name) == 0:
        raise ValueError("Cannot fetch agent with empty name")
    return registry[execution_key][name]


def del_agent(name, exec_key):
    """
    Delete an agent from the registry.
    Return: None
    """
    if exec_key is None:
        raise ValueError("Cannot delete agent without execution key")
    del registry[exec_key][name]
