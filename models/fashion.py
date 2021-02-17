"""
This is the Adam Smith fashion model.
"""

from lib.agent import MOVE
from lib.display_methods import BLUE, DARKRED, NAVY, RED
from lib.model import COLOR, MBR_ACTION, NUM_MBRS, NUM_MBRS_PROP, Model

DEBUG = False

MODEL_NAME = "fashion"
DEF_NUM_TSETTERS = 5
DEF_NUM_FOLLOWERS = 55


def tsetter_action(agent, **kwargs):
    """
    A simple default agent action for trend setters
    """
    if DEBUG:
        print("Agent {} is located at {}".format(agent.name,
                                                 agent.get_pos()))
    return MOVE


def follower_action(agent, **kwargs):
    """
    A simple default agent action for followers
    """
    if DEBUG:
        print("Agent {} is located at {}".format(agent.name,
                                                 agent.get_pos()))
    return MOVE


fashion_grps = {
    "Blue Trendsetters": {
        MBR_ACTION: tsetter_action,
        NUM_MBRS: DEF_NUM_TSETTERS,
        NUM_MBRS_PROP: "num_tsetters",
        COLOR: NAVY
    },
    "Red Trendsetters": {
        MBR_ACTION: tsetter_action,
        NUM_MBRS: DEF_NUM_TSETTERS,
        NUM_MBRS_PROP: "num_tsetters",
        COLOR: DARKRED
    },
    "Blue Followers": {
        MBR_ACTION: follower_action,
        NUM_MBRS: DEF_NUM_FOLLOWERS,
        NUM_MBRS_PROP: "num_followers",
        COLOR: BLUE
    },
    "Red Followers": {
        MBR_ACTION: follower_action,
        NUM_MBRS: DEF_NUM_FOLLOWERS,
        NUM_MBRS_PROP: "num_followers",
        COLOR: RED
    },
}


class Fashion(Model):
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
        return Fashion(serial_obj=serial_obj)
    else:
        return Fashion(MODEL_NAME, grp_struct=fashion_grps, props=props)


def main():
    model = create_model()
    model.run()
    return 0


if __name__ == "__main__":
    main()
