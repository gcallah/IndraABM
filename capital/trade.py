"""
A trade model.
Places two groups of agents in the enviornment randomly
and moves them around randomly.
"""

from indra.agent import Agent
from indra.composite import Composite
from indra.display_methods import BLUE
from indra.env import Env
from registry.registry import get_env, get_prop, user_log_notif
from indra.space import DEF_HEIGHT, DEF_WIDTH
from indra.utils import init_props, Debug
from capital.trade_utils import seek_a_trade
from capital.trade_utils import UTIL_FUNC, GEN_UTIL_FUNC, AMT_AVAIL
import capital.trade_utils as tu

MODEL_NAME = "trade"
DEF_NUM_TRADER = 4
DEF_NUM_RESOURCES = 20
DEF_NUM_RESOURCES_TYPE = 4
trader_group = None

max_utility = tu.max_util
GOODS = {"penguin": {AMT_AVAIL: DEF_NUM_RESOURCES,
                     UTIL_FUNC: GEN_UTIL_FUNC,
                     "incr": 0},
         "cat": {AMT_AVAIL: DEF_NUM_RESOURCES,
                 UTIL_FUNC: GEN_UTIL_FUNC,
                 "incr": 0},
         "bear": {AMT_AVAIL: DEF_NUM_RESOURCES,
                  UTIL_FUNC: GEN_UTIL_FUNC,
                  "incr": 0},
         "pet food": {AMT_AVAIL: DEF_NUM_RESOURCES,
                      UTIL_FUNC: GEN_UTIL_FUNC,
                      "incr": 0}
         }


def allocate_resources(trader, avail_goods):
    tu.endow(trader, avail_goods, rand=True)


def create_trader(name, i, props=None):
    return Agent(name + str(i), action=seek_a_trade,
                 attrs={"goods": {"penguin": {AMT_AVAIL: 0,
                                              UTIL_FUNC: "penguin_util_func",
                                              "incr": 0},
                                  "cat": {AMT_AVAIL: 0,
                                          UTIL_FUNC: "cat_util_func",
                                          "incr": 0},
                                  "bear": {AMT_AVAIL: 0,
                                           UTIL_FUNC: "bear_util_func",
                                           "incr": 0},
                                  "pet food": {AMT_AVAIL: 0,
                                               UTIL_FUNC: GEN_UTIL_FUNC,
                                               "incr": 0}
                                  },
                        "util": 0,
                        "pre_trade_util": 0,
                        "trades_with": "trader"})


def set_up(props=None):
    """
    A func to set up run that can also be used by test code.
    """
    global max_utility
    pa = init_props(MODEL_NAME, props, model_dir="capital")
    trader_group = Composite("trader", {"color": BLUE},
                             member_creator=create_trader,
                             props=pa,
                             num_members=get_prop('num_traders',
                                                  DEF_NUM_TRADER))
    Env("env",
        height=get_prop('grid_height', DEF_HEIGHT),
        width=get_prop('grid_width', DEF_WIDTH),
        members=[trader_group])
    for trader in trader_group:
        allocate_resources(trader_group[trader], GOODS)
        user_log_notif(trader_group[trader]["goods"])
    return (trader_group, max_utility)


def main():
    global trader_group
    global max_utility

    (trader_group, max_utility) = set_up()

    if Debug().debug2:
        user_log_notif(get_env().__repr__())

    get_env()()
    return 0


if __name__ == "__main__":
    main()
