"""
A model to simulate the spread of panic in a crowd.
"""

from lib.agent import DONT_MOVE, Agent
from lib.space import neighbor_ratio
from lib.display_methods import RED, GREEN
from lib.model import Model
from registry.registry import get_model

MODEL_NAME = "panic"
DEBUG = False  # turns debugging code on or off
DEBUG2 = False  # turns deeper debugging code on or off

DEF_DIM = 10
DEF_NUM_PEOPLE = DEF_DIM*DEF_DIM
DEF_NUM_PANIC = int(.3 * DEF_NUM_PEOPLE)
DEF_NUM_CALM = int(.7 * DEF_NUM_PEOPLE)

AGENT_PREFIX = "Agent"
THRESHHOLD = 2

CALM = "Calm"
PANIC = "Panic"


def is_calm(agent, *args):
    """
    Checking whether the agent is calm.
    """
    return agent.prim_group_nm() == CALM


def is_panicking(agent, *args):
    """
    Checking whether the agent is panicking.
    """
    return agent.prim_group_nm() == PANIC


def agent_action(agent, **kwargs):
    """
    This is what agents do each turn of the model.
    """
    ratio = neighbor_ratio(agent, pred_one=is_calm, pred_two=is_panicking)
    if ratio > THRESHHOLD:
        if DEBUG2:
            print("Changing the agent's group to panic!")
        agent.has_acted = True
        print("Agent's name is", agent)
        get_model(agent.exec_key).add_switch(str(agent), CALM, PANIC)
    return DONT_MOVE


def create_pagent(name, i, action=None, exec_key=None):
    return Agent(name + str(i),
                 exec_key=exec_key, action=action)


panic_grps = {
    CALM: {
        # "mbr_creator": create_pagent,
        "grp_action": None,
        "mbr_action": agent_action,
        "num_mbrs": DEF_NUM_CALM,
        "color": GREEN
    },
    PANIC: {
        # "mbr_creator": create_pagent,
        "grp_action": None,
        "mbr_action": agent_action,
        "num_mbrs": DEF_NUM_PANIC,
        "color": RED
    },
}


class Panic(Model):
    def handle_props(self, props):
        super().handle_props(props)
        grid_height = self.props.get("grid_height")
        grid_width = self.props.get("grid_width")
        num_agents = grid_height * grid_width
        pct_panic = self.props.get("pct_panic") / 100
        pct_calm = 1 - pct_panic
        self.grp_struct[CALM]["num_mbrs"] = int(pct_calm * num_agents)
        self.grp_struct[PANIC]["num_mbrs"] = int(pct_panic * num_agents)


def main():
    model = Panic(MODEL_NAME, grp_struct=panic_grps)
    model.run()
    return 0


if __name__ == "__main__":
    main()
