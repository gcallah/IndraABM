"""
A model to simulate the spread of fire in a forest.
"""
import random
from lib.agent import DONT_MOVE
from lib.space import neighbor_ratio
from lib.display_methods import RED, BLUE
from lib.model import Model

MODEL_NAME = "segregation"
DEBUG = False  # Turns debugging code on or off
DEBUG2 = False  # Turns deeper debugging code on or off

NUM_RED = 250
NUM_BLUE = 250

DEF_CITY_DIM = 40

TOLERANCE = "tolerance"
DEVIATION = "deviation"
GRP_INDEX = "grp_index"

DEF_HOOD_SIZE = 1
DEF_TOLERANCE = .5
DEF_SIGMA = .2

MIN_TOL = 0.1
MAX_TOL = 0.9

BLUE_GRP_IDX = 0
RED_GRP_IDX = 1

HOOD_SIZE = 4

NOT_ZERO = .001

BLUE_AGENTS = "Blue agents"
RED_AGENTS = "Red agents"

group_names = [BLUE_AGENTS, RED_AGENTS]

hood_size = None

opp_group = None


def get_tolerance(default_tolerance, sigma):
    """
    `tolerance` measures how *little* of one's own group one will
    tolerate being among.
    """
    tol = random.gauss(default_tolerance, sigma)
    # a low tolerance number here means high tolerance!
    tol = min(tol, MAX_TOL)
    tol = max(tol, MIN_TOL)
    return tol


def env_favorable(hood_ratio, my_tolerance):
    """
    Is the environment to our agent's liking or not??
    """
    return hood_ratio >= my_tolerance


def agent_action(agent, **kwargs):
    """
    This is what agents do each turn of the model.
    """
    agent_group = agent.group_name()
    ratio_num = neighbor_ratio(agent, # noqa F841
                               lambda agent: agent.group_name() == agent_group,
                               size=1)
    return DONT_MOVE


segregation_grps = {
    "blue_group": {
        "grp_action": None,
        "mbr_action": agent_action,
        "num_mbrs": NUM_BLUE,
        "num_mbs_prop": "num_blue",
        "color": BLUE
    },
    "red_group": {
        "grp_action": None,
        "mbr_action": agent_action,
        "num_members": NUM_RED,
        "num_mbrs_prop": "num_red",
        "color": RED
    },
}


class Segregation(Model):
    """
    Thomas Schelling's famous model of neighborhood segregation.
    """


def create_model(serial_obj=None):
    """
    This is for the sake of the API server:
    """
    if serial_obj is not None:
        return Segregation(serial_obj=serial_obj)
    else:
        return Segregation(MODEL_NAME, grp_struct=segregation_grps)


def main():
    model = create_model()
    model.run()
    return 0


if __name__ == "__main__":
    main()
