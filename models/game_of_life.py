
"""
This is a minimal model that inherits from model.py
and just sets up a couple of agents in two groups that
do nothing except move around randomly.
"""

from lib.display_methods import RED, BLUE
from lib.agent import DONT_MOVE
from lib.model import Model, create_agent

MODEL_NAME = "game_of_life"

DEF_NUM_ALIVE = 4
DEF_NUM_DEAD = 4


def game_agent_action(agent, **kwargs):
    """
    A simple default agent action.
    """
    print("Agent {} is acting".format(agent.name))
    return DONT_MOVE


GAME_GROUP_STRUCT = {
    "dead": {
        "mbr_creator": create_agent,
        "mbr_action": game_agent_action,
        "num_members": DEF_NUM_DEAD,
        "color": BLUE
    },
    "alive": {
        "mbr_creator": create_agent,
        "mbr_action": game_agent_action,
        "num_members": DEF_NUM_ALIVE,
        "color": RED
    },
}


class GameOfLife(Model):
    """
    This class should just create a basic model that runs, has
    some agents that move around, and allows us to test if
    the system as a whole is working.
    """
    def __init__(self, name=MODEL_NAME):
        super().__init__(name, grp_struct=GAME_GROUP_STRUCT)

    def run(self):
        print("My groups are:", self.groups)
        return super().run()


def main():
    model = GameOfLife()
    model.run()
    return 0


if __name__ == "__main__":
    main()
