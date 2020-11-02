"""
A model to simulate the spread of fire in a forest.
"""

from lib.agent import Agent, DONT_MOVE, switch
from lib.group import Group
from lib.space import neighbor_ratio
from lib.display_methods import RED, GREEN
from lib.display_methods import TREE
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


PANIC_GRP_STRUCT = {
    "calm_group": {
        "mbr_creator": create_agent,
        "mbr_action": agent_action,
        "num_members": DEF_NUM_PEOPLE,
        "color": GREEN
    },
    "panic_group": {
        "mbr_creator": create_agent,
        "mbr_action": agent_action,
        "num_members": DEF_NUM_PANIC,
        "color": RED
    },
}

class Panic(Model):

    def __init__(self, name=MODEL_NAME):
        super().__init__(name, grp_struct=PANIC_GRP_STRUCT)

    def run(self):
        print("My groups are:", self.groups)
        return super().run()

def main():
    model = Panic()
    model.run()
    return 0

if __name__ == "__main__":
    main()


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

# How do I get grid width and grid height from the props ?

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


def set_up(props=None):
    """
    A func to set up a  run that can also be used by test code.
    """
    init_props(MODEL_NAME, props)

    execution_key = int(props[EXEC_KEY].val) \
        if props is not None else CLI_EXEC_KEY

    grid_height = get_prop('grid_height', DEF_DIM,
                           execution_key=execution_key)
    grid_width = get_prop('grid_width', DEF_DIM, execution_key=execution_key)
    per_panic = get_prop('per_panic', DEF_PANIC, execution_key=execution_key)
    per_panic = per_panic/100
    groups = []
    calm = Composite(CALM, {"color": GREEN, "marker": TREE},
                     execution_key=execution_key)
    groups.append(calm)
    panic = Composite(PANIC, {"color": RED, "marker": TREE},
                      execution_key=execution_key)
    groups.append(panic)

    Env(MODEL_NAME, height=grid_height,
        width=grid_width, members=groups,
        execution_key=execution_key)

    
    # whereas these settings must be re-done every API re-load:
    set_env_attr(execution_key, CLI_EXEC_KEY)


if __name__ == "__main__":
    main()
