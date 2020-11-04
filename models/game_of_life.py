from lib.display_methods import RED, BLUE
from lib.agent import DONT_MOVE
from lib.model import Model, create_agent
from lib.group import Group
from lib.space import get_num_of_neighbors
from registry.registry import get_env

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
        "grp_action": None,
        "mbr_action": game_agent_action,
        "num_mbrs": DEF_NUM_DEAD,
        "num_mbrs_prop": "num_blue",
        "color": BLUE
    },
    "alive": {
        "mbr_creator": create_agent,
        "grp_action": None,
        "mbr_action": game_agent_action,
        "num_mbrs": DEF_NUM_ALIVE,
        "num_mbrs_prop": "num_red",
        "color": RED
    },
}


def populate_board(patterns, pattern_num):
    agent_locs = patterns[pattern_num]
    grp = GAME_GROUP_STRUCT["dead"]
    for loc in agent_locs:
        agent = create_agent(loc[x],loc[y],game_agent_action)
        grp += agents_to_create
        get_env().place_member(agent, xy=loc)


def create_groups(self):
    self.groups = []
    grps = self.grp_struct
    for grp_nm in self.grp_struct:
        grp = grps[grp_nm]
        self.groups.append(Group(grp_nm,
                           {"color": grp["color"]},
                           num_members=DEF_NUM_ALIVE,
                           mbr_creator=grp["mbr_creator"],
                           mbr_action=grp["mbr_action"]))
    return self.groups


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
        print("My groups are:", self.groups)
        return super().run()


def main():
    model = GameOfLife(MODEL_NAME, grp_struct=GAME_GROUP_STRUCT)
    model.run()
    return 0


if __name__ == "__main__":
    main()
