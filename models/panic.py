"""
A model to simulate the spread of fire in a forest.
"""

from lib.agent import DONT_MOVE
from lib.group import Group
# from lib.space import neighbor_ratio
from lib.display_methods import RED, GREEN
# from lib.env import Env
from lib.model import Model, create_agent
from lib.utils import init_props
# import random

MODEL_NAME = "panic"
DEBUG = False  # turns debugging code on or off
DEBUG2 = False  # turns deeper debugging code on or off

DEF_DIM = 10
DEF_NUM_PEOPLE = DEF_DIM*DEF_DIM
DEF_NUM_PANIC = int(.3 * DEF_NUM_PEOPLE)
DEF_NUM_CALM = int(.7 * DEF_NUM_PEOPLE)

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


def agent_action(agent, **kwargs):
    """
    This is what agents do each turn of the model.
    """
    # we need ration of panic neighbours to calm to be 1/2 in order for the
    # agent to start panicking
    # ratio = neighbor_ratio(agent, pred_one=is_calm,
    # pred_two=is_panicking)
    # hardcoding ratio value for now, until we manage to fix
    # neighbor_ratio method above
    ratio = 3
    # print("The ratio is ", ratio)
    if ratio > THRESHHOLD:
        if DEBUG2:
            print("Changing the agent's state to panic!")
        # print("Agent's state is being changed to Panic")
        agent["state"] = PN
        agent.has_acted = True
        # model.add_switch(agent, CALM, PANIC) ?
        # how do we access add_switch in model
    return DONT_MOVE


panic_grps = {
    "calm_group": {
        "mbr_creator": create_agent,
        "grp_action": None,
        "mbr_action": agent_action,
        "num_mbrs": DEF_NUM_CALM,
        "color": GREEN
    },
    "panic_group": {
        "mbr_creator": create_agent,
        "grp_action": None,
        "mbr_action": agent_action,
        "num_members": DEF_NUM_PANIC,
        "color": RED
    },
}


class Panic(Model):
    # overriding create groups method of the Model class using number of groups
    # calculated in the model.
    def create_groups(self, props=None):
        init_props(MODEL_NAME, props)
        self.groups = []
        grid_height = self.props.get("grid_height")
        grid_width = self.props.get("grid_width")
        num_agents = grid_height * grid_width
        per_panic = self.props.get("per_panic")/100
        perc_calm = 1 - per_panic
        num_calm_agents = int(perc_calm * num_agents)
        num_panic_agents = int(per_panic * num_agents)
        self.groups.append(Group("calm_group",
                                 action=None,
                                 color=GREEN,
                                 num_mbrs=num_calm_agents,
                                 mbr_creator=create_agent,
                                 mbr_action=agent_action,
                                 exec_key=self.exec_key))
        self.groups.append(Group("panic_group",
                                 action=None,
                                 color=RED,
                                 num_mbrs=num_panic_agents,
                                 mbr_creator=create_agent,
                                 mbr_action=agent_action,
                                 exec_key=self.exec_key))
        return self.groups


def main():
    model = Panic(MODEL_NAME, grp_struct=panic_grps)
    model.run()
    return 0


if __name__ == "__main__":
    main()
