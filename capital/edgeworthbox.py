
"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

from lib.agent import MOVE
from lib.display_methods import RED, BLUE
from lib.model import Model, NUM_MBRS, MBR_ACTION, NUM_MBRS_PROP, COLOR
from capital.trade_utils import seek_a_trade

DEBUG = False

MODEL_NAME = "edgeworthbox"
DEF_WINE_MBRS = 1
DEF_CHEESE_MBRS = 1


def trader_action(agent, **kwargs):
    """
    A simple default agent action.
    """
    if DEBUG:
        print("Agent {} is located at {}".format(agent.name,
                                                 agent.get_pos()))
    return MOVE


edge_grps = {
    "wine_grp": {
        MBR_CREATOR: create_wine,
        MBR_ACTION: seek_a_trade,
        NUM_MBRS: DEF_WINE_MBRS,
        COLOR: RED
    },
    "cheese_grp": {
        MBR_CREATOR: create_cheese,
        MBR_ACTION: seek_a_trade,
        NUM_MBRS: DEF_CHEESE_MBRS,
        COLOR: BLUE
    },
}


class EdgeworthBox(Model):
    """
    This class should just create a basic model that runs, has
    some agents that move around, and allows us to test if
    the system as a whole is working.
    It turns out that so far, we don't really need to subclass anything!
    """


def create_model(serial_obj=None, props=None):
    """
    This is for the sake of the API server:
    """
    if serial_obj is not None:
        return EdgeworthBox(serial_obj=serial_obj)
    else:
        return EdgeworthBox(MODEL_NAME, grp_struct=edge_grps, props=props)


def main():
    model = create_model()
    model.run()
    return 0


if __name__ == "__main__":
    main()
