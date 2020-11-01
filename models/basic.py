
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


basic_grps = {
    "blue_grp": {
        "mbr_creator": create_agent,
        "grp_action": None,
        "mbr_action": basic_action,
        "num_mbrs": DEF_BLUE_MBRS,
        "color": BLUE
    },
    "red_grp": {
        "mbr_creator": create_agent,
        "grp_action": None,
        "mbr_action": basic_action,
        "num_mbrs": DEF_RED_MBRS,
        "color": RED
    },
}


class Basic(Model):
    """
    This class should just create a basic model that runs, has
    some agents that move around, and allows us to test if
    the system as a whole is working.
    """
    def create_groups(self):
        """
        Must modify group struct from props.
        """
        self.grp_struct["blue_grp"]["num_mbrs"] = self.props.get("num_blue",
                                                                 DEF_BLUE_MBRS)
        print("num_blue = ", self.grp_struct["blue_grp"]["num_mbrs"])
        self.grp_struct["red_grp"]["num_mbrs"] = self.props.get("num_red",
                                                                DEF_BLUE_MBRS)
        return super().create_groups()


def main():
    model = Basic(MODEL_NAME, grp_struct=basic_grps)
    model.run()
    return 0


if __name__ == "__main__":
    main()
