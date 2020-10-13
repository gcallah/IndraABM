"""
This module contains the code for the base class of all Indra models.
"""
import os
from lib.utils import init_props
from lib.env import Env
from lib.user import TestUser, TermUser, TERMINAL, TEST

PROPS_PATH = "./props"


class Model():
    """
    This class is the base class for all Indra models.
    It will have all of the basic methods a model needs, as
    well as a `run()` method that will kick of the model,
    display the menu (if on a terminal), and register all
    methods necessary to be registered for the API server
    to work properly.
    """
    def __init__(self, model_nm="BaseModel", props=None):
        self.name = model_nm
        self.props = init_props(self.name, props)
        self.user_type = os.getenv("user_type", TERMINAL)
        self.create_user()
        self.groups = self.create_groups()
        self.env = self.create_env()

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
        self.user.tell("Running model " + self.name)
        return 0

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
