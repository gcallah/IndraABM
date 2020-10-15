"""
This module registers agent objects by name in a dictionary,
where the value should be the actual agent object. Since groups
and environments are agents, they should be registered here as
well.
While this is (right now) a simple dictionary, providing this
interface means that in the future, we can have something fancier,
if need be.
"""

agent_reg = {}


def reg_agent(name, agent):
    """
    Register an agent in the registry.
    Return: None
    """
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
