"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

import random
from lib.agent import MOVE  # , Agent 'not needed for now'
from lib.display_methods import RED, BLUE
from lib.model import Model

AT_HOME = "At home"
AT_BAR = "At bar"

MODEL_NAME = "el_farol"
DEF_AT_HOME = 2
DEF_AT_BAR = 2
DEF_MOTIV = 0.06
MOTIV = "motivation"


def get_decision(agent):
    """
    Decide whether to get wasted today or not
    """
    return random.random() <= agent[MOTIV]


def drinker_action(agent, **kwargs):
    """
    To go or not to go, that is the question -Not Callahan
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
