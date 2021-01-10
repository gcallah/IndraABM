"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

import random
from lib.agent import MOVE, Agent
from lib.env import Env
from lib.display_methods import RED, BLUE
from lib.model import Model, NUM_MBRS, MBR_ACTION
from lib.model import COLOR, MBR_CREATOR
from registry.registry import get_model
AT_HOME = "At home"
AT_BAR = "At bar"

MODEL_NAME = "el_farol"
DEF_AT_HOME = 2
DEF_AT_BAR = 2
DEF_MOTIV = 0.06
MOTIV = "motivation"
BAR_ATTEND = "bar attendees"


DEBUG = False


def get_decision(agent):
    """
    Decide whether to get wasted today or not
    """
    return random.random() <= agent[MOTIV]


def setup_attendance(pop_hist):
    """
    Set up our pop hist object to record exchanges per period.
    """
    if DEBUG:
        print("setting up attendance")
    pop_hist.record_pop(BAR_ATTEND, 0)


def drinker_action(agent, **kwargs):
    """
    To go or not to go, that is the question -Not Callahan
    for the now the decision is made at random
    """
    if DEBUG:
        print("Alcoholic {} is located at {}".format(agent.name,
                                                     agent.get_pos()))
    curr_model = get_model(agent.exec_key)
    if agent.group_name() == AT_HOME:
        # decid to go to bar or not
        if get_decision(agent):
            # drinker has motivation to go to bar today, consider him gone
            curr_model.add_switch(str(agent), AT_HOME, AT_BAR)
    else:
        # decide to leave bar or not
        if not get_decision(agent):
            # drinker has motivation to go toleave bar today, consider him gone
            curr_model.add_switch(str(agent), AT_BAR, AT_HOME)

    return MOVE


def create_drinker(name, i, exec_key=None, action=drinker_action):
    """
    Create a drinker
    """
    return Agent(name + str(i), attrs={MOTIV: DEF_MOTIV},
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
        at_bar = num_mbrs//2
        at_home = num_mbrs - at_bar
        self.grp_struct[AT_BAR]["num_mbrs"] = at_bar
        self.grp_struct[AT_HOME]["num_mbrs"] = at_home

    def create_env(self, env_action=None):
        """
        Overriding this method to  setup for pop_hist
        """
        self.env = Env(self.module, members=self.groups,
                       exec_key=self.exec_key, width=self.width,
                       height=self.height, action=env_action)
        return self.env


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
