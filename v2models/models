"""
A model to simulate the spread of fire in a forest.
"""

from lib.agent import Agent, DONT_MOVE, switch
from lib.group import Group
from lib.space import neighbor_ratio
from lib.display_methods import RED, GREEN
from lib.env import Env
from lib.model import Model, create_agent
from lib.utils import init_props
import random

MODEL_NAME = "panic"
DEBUG = False  # turns debugging code on or off
DEBUG2 = False  # turns deeper debugging code on or off

DEF_DIM = 10
DEF_NUM_PEOPLE = DEF_DIM*2
DEF_NUM_PANIC = .1 * DEF_NUM_PEOPLE

AGENT_PREFIX = "Agent"
THRESHHOLD = 2

# tree condition strings
STATE = "state"
CALM = "Clam"
PANIC = "Panic"

# state numbers: create as strings for JSON,
# convert to int when we need 'em that way
CM = "0"
PN = "1"


def is_calm(agent, *args):
    """
    Checking whether the state is healthy or not
    """
    return agent["state"] == CM


def is_panicking(agent, *args):
    """
    Checking whether the state is on fire or not
    """
    return agent["state"] == PN

# Does agent_action need to be outside of the Panic class ?
def agent_action(agent, **kwargs):
    """
    This is what trees do each turn in the forest.
    """
    # we need ration of panic neighbours to calm to be 1/2 in order for the
    # agent to start panicking
    ratio = neighbor_ratio(agent, pred_one=is_calm, pred_two=is_panicking)
    # print("The ratio is ", ratio)
    if ratio > THRESHHOLD:
        if DEBUG2:
            print("Changing the agent's state to panic!")
        # print("Agent's state is being changed to Panic")
        agent["state"] = PN
        agent.has_acted = True
        agent.add_switch(agent, CALM, PANIC)
    return DONT_MOVE

# What about the agent placement? Is it still working the same?

def place_agent(agent, state=CM, **kwargs):
    """
    Place a new agent.
    By default, they start out calm.
    """
    name = AGENT_PREFIX
    if(state == CM):
        agent = Agent(name,
                      action=agent_action,
                      attrs={"state": state,
                             "save_neighbors": True})
        return agent
    agent = Agent(name,
                  action=agent_action,
                  attrs={"state": state,
                         "save_neighbors": True})
    for x in range(grid_width):
        for y in range(grid_height):
            dist = random.random()
            if per_panic > dist:
                agent = Agent(name=("(%d,%d)" % (x, y)),
                              action=agent_action,
                              attrs={"state": PN,
                              "save_neighbors": True},
                              execution_key=execution_key)
                loc = eval(agent.name)
                panic += agent
                get_env().place_member(agent, xy=loc)
                # place_agent(agent, state=PN)
            else:
                agent = Agent(name=("(%d,%d)" % (x, y)),
                              action=agent_action,
                              attrs={"state": CM,
                              "save_neighbors": True},
                              execution_key=execution_key)
                loc = eval(agent.name)
                calm += agent
                get_env().place_member(agent, xy=loc)
                # place_agent(agent)
    return agent


panic_grps = {
    "calm_group": {
        "mbr_creator": create_agent,
        "grp_action": None,
        "mbr_action": agent_action,
        "num_mbrs": DEF_NUM_PEOPLE,
        "num_mbs_prop": "num_calm",
        "color": GREEN
    },
    "panic_group": {
        "mbr_creator": create_agent,
        "grp_action": None,
        "mbr_action": agent_action,
        "num_members": DEF_NUM_PANIC,
        "num_mbrs_prop": "num_panic",
        "color": RED
    },
}


class Panic(Model):


def main():
    model = Panic(MODEL_NAME, grp_struct=panic_grps)
    model.run()
    return 0


if __name__ == "__main__":
    main()