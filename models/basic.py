
"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

from lib.model import Model

MODEL_NAME = "basic"


class Basic(Model):
    """
    This class should just create a basic model that runs, has
    some agents that move around, and allows us to test if
    the system as a whole is working.
    """


def main():
    model = Basic(MODEL_NAME)
    model.run()
    return 0


if __name__ == "__main__":
    main()

