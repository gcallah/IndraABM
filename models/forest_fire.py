
"""
A model for how fires spread through a forest.
"""

from lib.agent import DONT_MOVE
from lib.display_methods import TOMATO, GREEN, RED, SPRINGGREEN, BLACK
from lib.model import Model

MODEL_NAME = "forest_fire"
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
    print("Agent {} is in the forest.".format(agent.name))
    return DONT_MOVE


ff_grps = {
    HEALTHY: {
        "mbr_action": tree_action,
        "num_mbrs": DEF_NUM_TREES,
        "color": GREEN,
    },
    NEW_FIRE: {
        "mbr_action": tree_action,
        "num_mbrs": 0,
        "color": TOMATO,
    },
    ON_FIRE: {
        "mbr_action": tree_action,
        "num_mbrs": 0,
        "color": RED,
    },
    BURNED_OUT: {
        "mbr_action": tree_action,
        "num_mbrs": 0,
        "color": BLACK,
    },
    NEW_GROWTH: {
        "mbr_action": tree_action,
        "num_mbrs": 0,
        "color": SPRINGGREEN,
    },
}


class ForestFire(Model):
    """
    The forest fire model.
    """


def main():
    model = ForestFire(MODEL_NAME, grp_struct=ff_grps)
    model.run()
    return 0


if __name__ == "__main__":
    main()
