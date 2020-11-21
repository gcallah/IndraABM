
"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

from lib.agent import MOVE
from lib.display_methods import RED, BLUE
from lib.model import Model

MODEL_NAME = "basic"
DEF_RED_MBRS = 2
DEF_BLUE_MBRS = 2
num_blue = 0


def basic_action(agent, **kwargs):
    """
    A simple default agent action.
    """
    print("Agent {} is located at {}".format(agent.name,
                                             agent.get_pos()))
    print("The number of blue agents is", num_blue)
    return MOVE


basic_grps = {
    "blue_grp": {
        "mbr_action": basic_action,
        "num_mbrs": DEF_BLUE_MBRS,
        "num_mbrs_prop": num_blue,
        "color": BLUE
    },
    "red_grp": {
        "mbr_action": basic_action,
        "num_mbrs": DEF_RED_MBRS,
        "num_mbrs_prop": "num_red",
        "color": RED
    },
}


class Basic(Model):
    """
    This class should just create a basic model that runs, has
    some agents that move around, and allows us to test if
    the system as a whole is working.
    It turns out that so far, we don't really need to subclass anything!
    """


def main():
    model = Basic(MODEL_NAME, grp_struct=basic_grps)
    model.run()
    return 0


if __name__ == "__main__":
    main()
