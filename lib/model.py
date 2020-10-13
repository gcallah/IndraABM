"""
This module contains the code for the base class of all Indra models.
"""
import os
from lib.utils import init_props
from lib.env import Env
from lib.user import TestUser, TermUser, TERMINAL, TEST
from lib.user import USER_EXIT

PROPS_PATH = "./props"
DEF_TIME = 10


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
    def __init__(self, model_nm="BaseModel", props=None):
        self.name = model_nm
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
            self.user = TermUser()
            self.user.tell("Welcome to Indra, " + str(self.user) + "!")
        elif self.user_type == TEST:
            self.user = TestUser()

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
            self.env()
            num_acts += 10   # should be a
            num_moves += 10  # should be m
            # census_rpt = self.get_census(num_moves)
            census_rpt = "Ran period {}". format(self.period)
            self.user.tell(census_rpt)
            self.num_switches = 0
        return num_acts

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
        return []

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
