"""
This module contains the code for the base class of all Indra models.
"""
import os
from lib.utils import init_props
from lib.agent import Agent, DONT_MOVE
from lib.composite import Composite
from lib.env import Env
from lib.user import TestUser, TermUser, TERMINAL, TEST
from lib.user import USER_EXIT
from lib.display_methods import RED, BLUE

PROPS_PATH = "./props"
DEF_TIME = 10
DEF_NUM_MEMBERS = 1


def def_agent_action(agent, **kwargs):
    """
    A simple default agent action.
    """
    print("Agent {} is acting".format(agent.name))
    return DONT_MOVE


def create_agent(name, i, action=def_agent_action, **kwargs):
    """
    Create an agent.
    """
    return Agent(name + str(i), action=action, kwargs=kwargs)


DEF_GROUP_STRUCT = {
    "blue_group": {
        "mbr_creator": create_agent,
        "num_members": DEF_NUM_MEMBERS,
        "color": BLUE
    },
    "red_group": {
        "mbr_creator": create_agent,
        "num_members": DEF_NUM_MEMBERS,
        "color": RED
    },
}


class Model():
    """
    This class is the base class for all Indra models.
    It will have all of the basic methods a model needs, as
    well as a `run()` method that will kick of the model,
    display the menu (if on a terminal), and register all
    methods necessary to be registered for the API server
    to work properly.
    It should also make the notebook generator much simpler,
    since the class methods will necessarily be present.
    """
    def __init__(self, model_nm="BaseModel", props=None,
                 grp_struct=DEF_GROUP_STRUCT):
        self.name = model_nm
        self.grp_struct = grp_struct
        self.props = init_props(self.name, props)
        self.user_type = os.getenv("user_type", TERMINAL)
        self.create_user()
        self.groups = self.create_groups()
        self.env = self.create_env()
        self.period = 0

    def create_user(self):
        """
        This will create a user of the correct type.
        """
        if self.user_type == TERMINAL:
            self.user = TermUser(model=self)
            self.user.tell("Welcome to Indra, " + str(self.user) + "!")
        elif self.user_type == TEST:
            self.user = TestUser(model=self)
        return self.user

    def create_env(self):
        """
        Override this method to create a unique env...
        but this one will already set the model name and add
        the groups.
        """
        self.env = Env(self.name, members=self.groups)
        return self.env

    def create_groups(self):
        """
        Override this method in your model to create all of your groups.
        """
        self.groups = []
        grps = self.grp_struct
        for grp_nm in self.grp_struct:
            self.groups.append(Composite(grp_nm,
                               {"color": grps[grp_nm]["color"]},
                               num_members=DEF_NUM_MEMBERS,
                               mbr_creator=grps[grp_nm]["mbr_creator"]))
        return self.groups

    def run(self, periods=None):
        """
        This method runs the model. If `periods` is not None,
        it will run it for that many periods. Otherwise, on
        a terminal, it will display the menu.
        Return: 0 if run was fine.
        """
        if (self.user is None) or (self.user_type == TEST):
            self.runN()
        else:
            self.user.tell("Running model " + self.name)
            while True:
                # run until user exit!
                if self.user() == USER_EXIT:
                    break

        return 0

    def runN(self, periods=DEF_TIME):
        """
            Run our model for N periods.
            Return the total number of actions taken.
        """
        num_acts = 0
        num_moves = 0
        for i in range(periods):
            self.period += 1
            # these things need to be done before action loop:
            # self.handle_womb()
            # self.handle_switches()
            # self.handle_pop_hist()

            # now we call upon the env to act:
            (num_acts, num_moves) = self.env()
            census_rpt = self.rpt_census(num_acts, num_moves)
            print(census_rpt)
            self.user.tell(census_rpt)
            self.num_switches = 0
        return num_acts

    def rpt_census(self, acts, moves):
        """
        This is the default census report.
        Return: a string saying what happened in a period.
        """
        return "In period {} there were {} actionsn".format(self.period,
                                                            acts)

    def from_json(self, serial_obj):
        """
        This method restores a model from its JSON rep.
        """
        self.name = serial_obj["name"]

    def to_json(self):
        """
        This method generates the JSON representation for this model.
        """
        rep = {}
        rep["name"] = self.name
        return rep


def main():
    model = Model()
    model.run()
    return 0


if __name__ == "__main__":
    main()
