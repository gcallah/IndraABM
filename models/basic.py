
"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

from lib.agent import MOVE
from lib.display_methods import RED, BLUE
from lib.model import Model, create_agent

MODEL_NAME = "basic"
DEF_RED_MBRS = 2
DEF_BLUE_MBRS = 2


def basic_action(agent, **kwargs):
    """
    A simple default agent action.
    """
    print("Agent {} is located at {}".format(agent.name,
                                             agent.get_pos()))
    return MOVE


BASIC_GRP_STRUCT = {
    "blue_group": {
        "mbr_creator": create_agent,
        "mbr_action": basic_action,
        "num_members": DEF_BLUE_MBRS,
        "color": BLUE
    },
    "red_group": {
        "mbr_creator": create_agent,
        "mbr_action": basic_action,
        "num_members": DEF_RED_MBRS,
        "color": RED
    },
}


class Basic(Model):
    """
    This class should just create a basic model that runs, has
    some agents that move around, and allows us to test if
    the system as a whole is working.
    """
    def __init__(self, name=MODEL_NAME):
        super().__init__(name, grp_struct=BASIC_GRP_STRUCT)

    def run(self):
        print("My groups are:", self.groups)
        return super().run()


def main():
    model = Basic()
    model.run()
    return 0


if __name__ == "__main__":
    main()
