
"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

from lib.agent import MOVE
from lib.display_methods import RED, BLUE
from lib.model import Model

AT_HOME = "At home"
AT_BAR = "At bar"

MODEL_NAME = "el_farol"
DEF_AT_HOME = 2
DEF_AT_BAR = 2


def drinker_action(agent, **kwargs):
    """
    A simple default agent action.
    """
    print("Alcoholic {} is located at {}".format(agent.name,
                                                 agent.get_pos()))
    return MOVE


el_farol_grps = {
    AT_HOME: {
        "mbr_action": drinker_action,
        "num_mbrs": DEF_AT_HOME,
        "color": BLUE
    },
    AT_BAR: {
        "mbr_action": drinker_action,
        "num_mbrs": DEF_AT_BAR,
        "color": RED
    },
}


class ElFarol(Model):
    """
    The El Farol bar: a great place to be, unless everyone else goes there
    also!
    """


def main():
    model = ElFarol(MODEL_NAME, grp_struct=el_farol_grps)
    model.run()
    return 0


if __name__ == "__main__":
    main()
