
"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

from lib.agent import MOVE
from lib.display_methods import TOMATO, GREEN
# from lib.display_methods import SPRINGGREEN, TOMATO, TREE, BLACK
from lib.model import Model

MODEL_NAME = "forestfire"
DEF_NUM_TREES = 10

# tree group names
HEALTHY = "Healthy"
NEW_FIRE = "New Fire"
ON_FIRE = "On Fire"
BURNED_OUT = "Burned Out"
NEW_GROWTH = "New Growth"


def tree_action(agent, **kwargs):
    """
    A simple default agent action.
    """
    print("Agent {} is located at {}".format(agent.name,
                                             agent.get_pos()))
    return MOVE


forest_grps = {
    HEALTHY: {
        "mbr_action": tree_action,
        "num_mbrs": DEF_NUM_TREES,
        "color": GREEN
    },
    NEW_FIRE: {
        "mbr_action": tree_action,
        "num_mbrs": 2,
        "color": TOMATO
    },
}


class ForestFire(Model):
    """
    This class should just create a basic model that runs, has
    some agents that move around, and allows us to test if
    the system as a whole is working.
    It turns out that so far, we don't really need to subclass anything!
    """


def main():
    model = ForestFire(MODEL_NAME, grp_struct=forest_grps)
    model.run()
    return 0


if __name__ == "__main__":
    main()
