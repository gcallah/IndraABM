
"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

from lib.agent import Agent
from lib.display_methods import RED, BLUE
from lib.model import Model, NUM_MBRS, MBR_CREATOR, MBR_ACTION, COLOR
from capital.trade_utils import GEN_UTIL_FUNC, UTIL_FUNC, AMT_AVAIL
from capital.trade_utils import seek_a_trade

DEBUG = False

MODEL_NAME = "edgeworthbox"
DEF_WINE_MBRS = 1
DEF_CHEESE_MBRS = 1
DEF_NUM_CHEESE = 4
DEF_NUM_WINE = 4

GOODS = "goods"
INCR = "incr"


def create_wine(name, i, action=None, **kwargs):
    start_wine = DEF_NUM_WINE
    # if props is not None:
    #     start_wine = props.get('start_wine',
    #                            DEF_NUM_WINE)
    return Agent(name + str(i),
                 action=seek_a_trade,
                 attrs={GOODS: {"wine": {AMT_AVAIL: start_wine,
                                         UTIL_FUNC: GEN_UTIL_FUNC,
                                         INCR: 0},
                                "cheese": {AMT_AVAIL: 0,
                                           UTIL_FUNC: GEN_UTIL_FUNC,
                                           INCR: 0}},
                        "util": 0,
                        "pre_trade_util": 0,
                        "trades_with": "Cheese holders"},
                 **kwargs)


def create_cheese(name, i, action=None, **kwargs):
    start_cheese = DEF_NUM_CHEESE
    # if props is not None:
    #     start_cheese = props.get('start_cheese',
    #                              DEF_NUM_CHEESE)
    return Agent(name + str(i),
                 action=seek_a_trade,
                 attrs={GOODS: {"cheese": {AMT_AVAIL: start_cheese,
                                           UTIL_FUNC: GEN_UTIL_FUNC,
                                           INCR: 0},
                                "wine": {AMT_AVAIL: 0,
                                         UTIL_FUNC: GEN_UTIL_FUNC,
                                         INCR: 0}},
                        "util": 0,
                        "pre_trade_util": 0,
                        "trades_with": "Wine holders"},
                 **kwargs)


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
    def handle_props(self, props, model_dir=None):
        super().handle_props(props, model_dir='capital')

    def create_groups(self):
        grps = super().create_groups()
        return grps


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
