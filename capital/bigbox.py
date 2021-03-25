
"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

from lib.agent import MOVE, Agent
from lib.display_methods import BLACK, BLUE, GREEN, RED, ORANGE, PURPLE
from lib.model import Model, NUM_MBRS, MBR_ACTION, NUM_MBRS_PROP, COLOR
from lib.utils import Debug
import random

DEBUG = Debug()

MODEL_NAME = "bigbox"
NUM_OF_CONSUMERS = 50
NUM_OF_MP = 8
DEBUG = False

MIN_CONSUMER_SPENDING = 50
MAX_CONSUMER_SPENDING = 70

BIG_BOX = "Big box"
CONSUMER = "Consumer"
HOOD_SIZE = 2
MP_PREF = 0.1
PERIOD = 7
STANDARD = 200
MULTIPLIER = 10

bb_capital = 1000
bb_expense = 100
item_needed = None

cons_goods = ["books", "coffee", "groceries", "hardware", "meals"]

mp_stores = {"Bookshop": {"color": ORANGE,
                          "per_expense": 20,
                          "init_capital": 90,
                          "goods_sold": ["books"]},
             "Coffeeshop": {"color": BLACK,
                            "per_expense": 22,
                            "init_capital": 100,
                            "goods_sold": ["coffee"], },
             "Grocery store": {"color": GREEN,
                               "per_expense": 23,
                               "init_capital": 100,
                               "goods_sold": ["groceries"], },
             "Hardware": {"color": RED,
                          "per_expense": 18,
                          "init_capital": 110,
                          "goods_sold": ["hardware"], },
             "Restaurant": {"color": PURPLE,
                            "per_expense": 25,
                            "init_capital": 100,
                            "goods_sold": ["meals"], }}


def get_rand_good():
    """
    Randomly select consumer's item needed
    after each run.
    """
    return random.choice(cons_goods)


def create_consumer(name, i, props=None, **kwargs):
    """
    Create consumers
    """
    spending_power = random.randint(MIN_CONSUMER_SPENDING,
                                    MAX_CONSUMER_SPENDING)
    consumer_books = {"spending power": spending_power,
                      "last util": 0.0,
                      "item needed": get_rand_good()}
    return Agent(name + str(i), attrs=consumer_books,
                 action=consumer_action, **kwargs)


def create_mp(store_grp, i, props=None, **kwargs):
    """
    Create a mom and pop store.
    """
    return Agent(name=str(store_grp) + " " + str(i),
                 attrs={"expense": mp_stores[store_grp]["per_expense"],
                        "capital": mp_stores[store_grp]["init_capital"]},
                 action=mp_action, **kwargs)


def consumer_action(agent, **kwargs):
    """
    Default basic model. To be fixed in next meeting
    """
    if DEBUG.debug:
        print("Agent {} is located at {}".format(agent.name,
                                                 agent.get_pos()))
    return MOVE


def mp_action(agent, **kwargs):
    """
    Default basic model. To be fixed in next meeting
    """
    if DEBUG.debug:
        print("Agent {} is located at {}".format(agent.name,
                                                 agent.get_pos()))
    return MOVE


bigbox_grps = {
    "consumer_grp": {
        MBR_ACTION: consumer_action,
        NUM_MBRS: NUM_OF_CONSUMERS,
        NUM_MBRS_PROP: "num_consumers",
        COLOR: BLUE
    },
    "mp_grp": {
        MBR_ACTION: mp_action,
        NUM_MBRS: NUM_OF_MP,
        NUM_MBRS_PROP: "num_mp",
        COLOR: RED
    },
}


class BigBox(Model):
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
        return BigBox(serial_obj=serial_obj)
    else:
        return BigBox(MODEL_NAME, grp_struct=bigbox_grps, props=props)


def main():
    model = create_model()
    model.run()

    return 0


if __name__ == "__main__":
    main()
