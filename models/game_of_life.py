from lib.display_methods import RED, BLUE
from lib.agent import DONT_MOVE
from lib.model import Model, create_agent
from lib.group import Group

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


class GameOfLife(Model):
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