
"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

from lib.model import Model
from indra.composite import Composite
from indra.display_methods import RED, BLUE


MODEL_NAME = "basic"


class Basic(Model):
    """
    This class should just create a basic model that runs, has
    some agents that move around, and allows us to test if
    the system as a whole is working.
    """
    def __init__(self, name=MODEL_NAME):
        super().__init__(name)

    def create_groups(self):
        self.groups = []
        self.groups.append(Composite("Blues", {"color": BLUE}))
        self.groups.append(Composite("Reds", {"color": RED}))
        return self.groups

    def run(self):
        super().run()
        print("My groups are:", self.groups)


def main():
    model = Basic()
    model.run()
    return 0


if __name__ == "__main__":
    main()

