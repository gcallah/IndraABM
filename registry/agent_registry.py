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
"""
from lib.agent import Agent

agent_reg = {}


def reg_agent(name, agent):
    """
    Register an agent in the registry.
    Raises an exception if `agent` is not an `Agent`.
    Return: None
    """
    if not isinstance(agent, Agent):
        raise ValueError("Object being registered is not an agent.")
    agent_reg[name] = agent


def get_agent(name):
    """
    Fetch an agent from the registry.
    Return: The agent object.
    """
    return agent_reg[name]


def del_agent(name):
    """
    Delete an agent from the registry.
    Return: None
    """
    del agent_reg[name]
