
"""
A model for how fires spread through a forest.
"""

from lib.agent import DONT_MOVE, Agent
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

# state numbers: create as strings for JSON,
# convert to int when we need 'em that way
HE = "0"
NF = "1"
OF = "2"
BO = "3"
NG = "4"


def is_healthy(agent, *args):
    """
    Checking whether the agent is healthy or not
    """
    return agent["state"] == HE


def is_on_fire(agent, *args):
    """
    Checking whether the agent is on fire or not
    """
    return agent["state"] == OF


def tree_action(agent, **kwargs):
    """
    A simple default agent action.
    """
    print("Agent {} is in the forest.".format(agent.name))
    return DONT_MOVE


def plant_tree(name, i, action=tree_action, state=HE, exec_key=None):
    return Agent(name + str(i), attrs={"state": state},
                 exec_key=exec_key, action=action)


ff_grps = {
    HEALTHY: {
        "mbr_creator": plant_tree,
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
    def handle_props(self, props):
        super().handle_props(props)
        height = self.props.get("grid_height")
        width = self.props.get("grid_width")
        density = self.props.get("density")
        num_agents = int(height * width * density)
        self.grp_struct[HEALTHY]["num_mbrs"] = num_agents


def main():
    model = ForestFire(MODEL_NAME, grp_struct=ff_grps)
    model.run()
    return 0


if __name__ == "__main__":
    main()
