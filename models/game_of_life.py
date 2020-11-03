from lib.display_methods import RED, BLUE
from lib.agent import DONT_MOVE
from lib.model import Model, MBR_ACTION
from lib.space import get_num_of_neighbors
from registry.registry import get_agent

MODEL_NAME = "game_of_life"

DEF_NUM_ALIVE = 4
DEF_NUM_DEAD = 4

DEAD = "dead"
ALIVE = "alive"


def is_dead(agent):
    return agent.prim_group == DEAD


def game_of_life_action(biosphere, **kwargs):
    dead_grp = get_agent(DEAD, biosphere.exec_key)
    print("Dead grp is:", repr(dead_grp))


def game_agent_action(agent, **kwargs):
    """
    A simple default agent action.
    """
    print("GofL agent {} is acting".format(agent.name))
    return DONT_MOVE


game_group_struct = {
    DEAD: {
        "num_mbrs": DEF_NUM_DEAD,
        "num_mbrs_prop": "num_blue",
        "color": BLUE
    },
    ALIVE: {
        MBR_ACTION: game_agent_action,
        "num_mbrs": DEF_NUM_ALIVE,
        "num_mbrs_prop": "num_red",
        "color": RED
    },
}


def live_or_die(agent):
    """
    Apply the rules for live agents.
    The agent passed in should be alive, meaning its color should be black.
    """
    num_live_neighbors = get_num_of_neighbors(exclude_self=True, pred=None,
                                              size=1, region_type=None)
    if (num_live_neighbors != 2 and num_live_neighbors != 3):
        return BLUE
    else:
        return RED


class GameOfLife(Model):
    def run(self):
        return super().run()


def main():
    model = GameOfLife(MODEL_NAME, grp_struct=game_group_struct,
                       env_action=game_of_life_action)
    model.run()
    return 0


if __name__ == "__main__":
    main()
