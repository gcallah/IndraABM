"""
This is the Adam Smith fashion model.
"""

# from lib.agent import MOVE
from lib.display_methods import BLUE, DARKRED, NAVY, RED
from lib.model import COLOR, MBR_ACTION, NUM_MBRS, NUM_MBRS_PROP, Model
from lib.utils import Debug

# from registry.registry import get_model

MODEL_NAME = "fashion"
DEF_NUM_TSETTERS = 5
DEF_NUM_FOLLOWERS = 55


def fashion_action(agent, **kwargs):
    """
    A simple default agent action
    """
    if Debug().debug:
        print("Agent", str(agent), "is acting.")

    # model = get_model(agent.exec_key)
    # num_others_red = len(others_red.subset(in_hood, agent, HOOD_SIZE))
    # num_others_blue = len(others_blue.subset(in_hood, agent, HOOD_SIZE))
    # total_others = num_others_red + num_others_blue
    # if total_others <= 0:
    #     return False

    # env_color = ratio_to_sin(num_others_red / total_others)

    # agent[COLOR_PREF] = new_color_pref(agent[COLOR_PREF], env_color)
    # if env_unfavorable(agent[DISPLAY_COLOR], agent[COLOR_PREF], op1, op2):
    #     change_color(agent, get_env(execution_key=execution_key), opp_group)
    #     return True
    # else:
    #     return False


fashion_grps = {
    "Blue Trendsetters": {
        MBR_ACTION: fashion_action,
        NUM_MBRS: DEF_NUM_TSETTERS,
        NUM_MBRS_PROP: "num_tsetters",
        COLOR: NAVY
    },
    "Red Trendsetters": {
        MBR_ACTION: fashion_action,
        NUM_MBRS: DEF_NUM_TSETTERS,
        NUM_MBRS_PROP: "num_tsetters",
        COLOR: DARKRED
    },
    "Blue Followers": {
        MBR_ACTION: fashion_action,
        NUM_MBRS: DEF_NUM_FOLLOWERS,
        NUM_MBRS_PROP: "num_followers",
        COLOR: BLUE
    },
    "Red Followers": {
        MBR_ACTION: fashion_action,
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
