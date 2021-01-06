
"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

from lib.agent import Agent, MOVE
from lib.display_methods import GREEN
from lib.model import Model, MBR_CREATOR, NUM_MBRS, MBR_ACTION  # , GRP_ACTION
from lib.model import NUM_MBRS_PROP, COLOR
# import capital.trade_utils as tu
from capital.trade_utils import seek_a_trade, GEN_UTIL_FUNC
from capital.trade_utils import AMT_AVAIL, endow, UTIL_FUNC  # , trader_debug

MODEL_NAME = "money"

DEF_NUM_TRADERS = 4

MONEY_MAX_UTIL = 100

DUR = "durability"
TRADE_COUNT = "trade_count"
INIT_COUNT = 0  # a starting point for trade_count

# a counter for counting number of continuous periods with no trade
eq_count = 0
# a dictionary storing the "trade_count" for each good from the last period
prev_trade = {'cow': 0,
              'gold': 0,
              'cheese': 0,
              'banana': 0,
              'diamond': 0,
              'avocado': 0,
              'stone': 0,
              'milk': 0,
              }

# these are the goods we hand out at the start:
natures_goods = {
    # add initial value to this data?
    # color choice isn't working yet, but we want to build it in
    "cow": {AMT_AVAIL: 100, UTIL_FUNC: GEN_UTIL_FUNC,
            "incr": 0, DUR: 0.8, "divisibility": 1.0,
            "trade_count": 0, "is_allocated": False,
            "age": 1, },
    "cheese": {AMT_AVAIL: 100, UTIL_FUNC: GEN_UTIL_FUNC,
               "incr": 0, DUR: 0.5, "divisibility": 0.4,
               "trade_count": 0, "is_allocated": False,
               "age": 1, },
    "gold": {AMT_AVAIL: 100, UTIL_FUNC: GEN_UTIL_FUNC,
             "incr": 0, DUR: 1.0, "divisibility": 0.05,
             "trade_count": 0, "is_allocated": False,
             "age": 1, },
    "banana": {AMT_AVAIL: 100, UTIL_FUNC: GEN_UTIL_FUNC,
               "incr": 0, DUR: 0.2, "divisibility": 0.2,
               "trade_count": 0, "is_allocated": False,
               "age": 1, },
    "diamond": {AMT_AVAIL: 100, UTIL_FUNC: GEN_UTIL_FUNC,
                "incr": 0, DUR: 1.0, "divisibility": 0.8,
                "trade_count": 0, "is_allocated": False,
                "age": 1, },
    "avocado": {AMT_AVAIL: 100, UTIL_FUNC: GEN_UTIL_FUNC,
                "incr": 0, DUR: 0.3, "divisibility": 0.5,
                "trade_count": 0, "is_allocated": False,
                "age": 1, "color": GREEN},
    "stone": {AMT_AVAIL: 100, UTIL_FUNC: GEN_UTIL_FUNC,
              "incr": 0, DUR: 1.0, "divisibility": 1.0,
              "trade_count": 0, "is_allocated": False,
              "age": 1, },
    "milk": {AMT_AVAIL: 100, UTIL_FUNC: GEN_UTIL_FUNC,
             "incr": 0, DUR: 0.2, "divisibility": 0.15,
             "trade_count": 0, "is_allocated": False,
             "age": 1, },
}


class Good:
    def __init__(self, name, amt, age=0):
        self.amt = amt
        self.dur_decr = natures_goods[name][DUR]
        self.util_func = natures_goods[name][UTIL_FUNC]
        self.age = age

    def get_decr_amt(self):
        return self.dur_decr * self.age

    def decay(self):
        self.age += 1


def create_trader(name, i, action=None, **kwargs):
    """
    A func to create a trader.
    """
    return Agent(name + str(i),
                 action=action,
                 # goods will now be a dictionary like:
                 # goods["cow"] = [cowA, cowB, cowC, etc.]
                 attrs={"goods": {},
                        "util": 0,
                        "pre_trade_util": 0},
                 **kwargs)


def trader_action(agent, **kwargs):
    """
    A simple default agent action.
    """
    seek_a_trade(agent, **kwargs)
    for good in natures_goods:
        # update current period's trade count in natures_good
        natures_goods[good][TRADE_COUNT] += agent["goods"][good][TRADE_COUNT]
        # return agent's trade_count to 0
        agent["goods"][good][TRADE_COUNT] = 0
        # increment every good's age by one each period
        agent["goods"][good]["age"] += 1
    return MOVE


money_grps = {
    "traders": {
        MBR_CREATOR: create_trader,
        MBR_ACTION: trader_action,
        NUM_MBRS: DEF_NUM_TRADERS,
        NUM_MBRS_PROP: "num_traders",
        COLOR: GREEN,
    },
}


def nature_to_traders(traders, nature):
    """
    A func to do the initial endowment from nature to all traders
    """
    for trader in traders:
        endow(traders[trader], nature)
        for good in traders[trader]["goods"]:
            if traders[trader]["goods"][good][AMT_AVAIL] != 0:
                nature[good]["is_allocated"] = True
        print(repr(traders[trader]))


TRADER_GRP = 0


class Money(Model):
    """
    The model class for the Menger money model.
    """
    def handle_props(self, props, model_dir=None):
        super().handle_props(props, model_dir='capital')

    def create_groups(self):
        grps = super().create_groups()
        nature_to_traders(grps[TRADER_GRP], natures_goods)
        return grps


def create_model(serial_obj=None, props=None):
    """
    This is for the sake of the API server:
    """
    if serial_obj is not None:
        return Money(serial_obj=serial_obj)
    else:
        return Money(MODEL_NAME, grp_struct=money_grps, props=props)


def main():
    model = create_model()
    model.run()
    return 0


if __name__ == "__main__":
    main()
