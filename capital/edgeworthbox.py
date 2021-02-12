
"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

from lib.agent import Agent
from lib.display_methods import RED, BLUE
from lib.model import Model, NUM_MBRS, MBR_CREATOR, MBR_ACTION, COLOR
from registry.registry import get_agent
from capital.trade_utils import GEN_UTIL_FUNC, UTIL_FUNC, AMT_AVAIL
from capital.trade_utils import seek_a_trade

DEBUG = False

MODEL_NAME = "edgeworthbox"
DEF_WINE_MBRS = 1
DEF_CHEESE_MBRS = 1
DEF_NUM_CHEESE = 4
DEF_NUM_WINE = 4

UTIL = "util"
PRE_TRADE_UTIL = "pre_trade_util"
TRADE_WITH = "trades_with"

GOODS = "goods"
INCR = "incr"

WINE_AGENT = "Wine agent"
CHEESE_AGENT = "Cheese agent"


def create_wine(name, i, action=None, **kwargs):
    start_wine = DEF_NUM_WINE
    # if props is not None:
    #     start_wine = props.get('start_wine',
    #                            DEF_NUM_WINE)
    return Agent(WINE_AGENT,
                 action=seek_a_trade,
                 attrs={GOODS: {"wine": {AMT_AVAIL: start_wine,
                                         UTIL_FUNC: GEN_UTIL_FUNC,
                                         INCR: 0},
                                "cheese": {AMT_AVAIL: 0,
                                           UTIL_FUNC: GEN_UTIL_FUNC,
                                           INCR: 0}},
                        UTIL: 0,
                        PRE_TRADE_UTIL: 0,
                        TRADE_WITH: "Cheese holders"},
                 **kwargs)


def create_cheese(name, i, action=None, **kwargs):
    start_cheese = DEF_NUM_CHEESE
    # if props is not None:
    #     start_cheese = props.get('start_cheese',
    #                              DEF_NUM_CHEESE)
    return Agent(CHEESE_AGENT,
                 action=seek_a_trade,
                 attrs={GOODS: {"cheese": {AMT_AVAIL: start_cheese,
                                           UTIL_FUNC: GEN_UTIL_FUNC,
                                           INCR: 0},
                                "wine": {AMT_AVAIL: 0,
                                         UTIL_FUNC: GEN_UTIL_FUNC,
                                         INCR: 0}},
                        UTIL: 0,
                        PRE_TRADE_UTIL: 0,
                        TRADE_WITH: "Wine holders"},
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

    def rpt_census(self, acts, moves):
        """
        This is where we override the default census report.
        """
        cheesey = get_agent(CHEESE_AGENT, exec_key=self.exec_key)
        winey = get_agent(WINE_AGENT, exec_key=self.exec_key)
        return (f"Wine and cheese holdings\n{cheesey}\n{winey}")


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
