"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

import random
from lib.agent import MOVE, Agent
from lib.display_methods import RED, BLUE
from lib.model import Model, NUM_MBRS, MBR_ACTION
from lib.model import COLOR, MBR_CREATOR
from registry.registry import get_model
AT_HOME = "At home"
AT_BAR = "At bar"

MODEL_NAME = "el_farol"
DEF_AT_HOME = 2
DEF_AT_BAR = 2
DEF_MOTIV = 0.6
MOTIV = "motivation"
BAR_ATTEND = "bar attendees"
DISC_AMT = .01
MIN_MOTIV = 0.05
MAX_MOTIV = .95
DEBUG = False
OPT_OCUPANCY = 0.6


def get_decision(agent):
    """
    Decide whether to get wasted today or not
    """
    return random.random() <= agent[MOTIV]


def discourage(agent):
    """
    Discourage an agent from going to bar
    """
    agent[MOTIV] = max(agent[MOTIV] - DISC_AMT, MIN_MOTIV)
    discouraged = not (get_decision(agent))
    return discouraged


def encourage(agent):
    """
    inrease motivation and try to change decision
    """
    agent[MOTIV] = min(agent[MOTIV] + DISC_AMT, MAX_MOTIV)
    encouraged = get_decision(agent)
    return encouraged


def drinker_action(agent, **kwargs):
    """
    To go or not to go, that is the question -Not Callahan
    for the now the decision is made at random
    """
    if DEBUG:
        print("Alcoholic {} is located at {}".format(agent.name,
                                                     agent.get_pos()))
    bar = get_model(agent.exec_key)
    attandance = bar.env.pop_hist.pops[AT_BAR]
    population = (bar.grp_struct[AT_BAR]["num_mbrs"] +
                  bar.grp_struct[AT_HOME]["num_mbrs"])
    last_night_full = attandance[-1] >= int(population * OPT_OCUPANCY)
    going = get_decision(agent)
    # for people at home
    if agent.group_name() == AT_HOME:
        # if last night was full, discourage going, else encourage
        if going and not last_night_full:
            # drinker has motivation to go to bar today, consider him gone
            bar.add_switch(str(agent), AT_HOME, AT_BAR)
        elif not going and not last_night_full:
            encouraged = encourage(agent)
            if encouraged:
                bar.add_switch(str(agent), AT_HOME, AT_BAR)
    else:
        # for people that went yesterday
        # if last night was full, discourage going, else encourage
        if going and last_night_full:
            # drinker has motivation to go toleave bar today, consider him gone
            discouraged = discourage(agent)
            if discouraged:
                bar.add_switch(str(agent), AT_BAR, AT_HOME)
        elif not going:
            bar.add_switch(str(agent), AT_BAR, AT_HOME)
    return MOVE


def create_drinker(name, i, exec_key=None, action=drinker_action):
    """
    Create a drinker
    drinkers starts with a random motivation
    """
    rand_motive = random.random()
    return Agent(name + str(i), attrs={MOTIV: rand_motive},
                 action=action, exec_key=exec_key)


el_farol_grps = {
    AT_HOME: {
        MBR_CREATOR: create_drinker,
        MBR_ACTION: drinker_action,
        NUM_MBRS: DEF_AT_HOME,
        COLOR: BLUE
    },
    AT_BAR: {
        MBR_CREATOR: create_drinker,
        MBR_ACTION: drinker_action,
        NUM_MBRS: DEF_AT_BAR,
        COLOR: RED
    },
}


class ElFarol(Model):
    """
    The El Farol bar: a great place to be, unless everyone else goes there
    also!
    """
    def handle_props(self, props):
        super().handle_props(props)
        # get total population and set  people at home and bar 50/50-ish
        num_mbrs = self.props.get("population")
        at_bar = int(num_mbrs * random.random())
        at_home = num_mbrs - at_bar
        self.grp_struct[AT_BAR]["num_mbrs"] = at_bar
        self.grp_struct[AT_HOME]["num_mbrs"] = at_home


def create_model(serial_obj=None, props=None):
    """
    This is for the sake of the API server:
    """
    if serial_obj is not None:
        return ElFarol(serial_obj=serial_obj)
    else:
        return ElFarol(MODEL_NAME, grp_struct=el_farol_grps, props=props)


def main():
    model = create_model()
    model.run()
    return 0


if __name__ == "__main__":
    main()
