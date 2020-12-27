"""
A model to simulate the spread of panic in a crowd.
"""

from lib.agent import DONT_MOVE
from lib.space import neighbor_ratio
from lib.display_methods import RED, GREEN
from lib.model import Model
from registry.registry import get_model

MODEL_NAME = "panic"
DEBUG = False  # turns debugging code on or off
DEBUG2 = False  # turns deeper debugging code on or off

DEF_DIM = 10
DEF_NUM_PEOPLE = DEF_DIM*DEF_DIM
DEF_NUM_PANIC = int(.3 * DEF_NUM_PEOPLE)
DEF_NUM_CALM = int(.7 * DEF_NUM_PEOPLE)

AGENT_PREFIX = "Agent"
THRESHHOLD = .2

CALM = "Calm"
PANIC = "Panic"


def agent_action(agent, **kwargs):
    """
    This is what agents do each turn of the model.
    """
    ratio = neighbor_ratio(agent, lambda agent: agent.group_name() == PANIC)
    if ratio > THRESHHOLD:
        if DEBUG2:
            print("Changing the agent's group to panic!")
        agent.has_acted = True
        if agent.group_name() == CALM:
            get_model(agent.exec_key).add_switch(str(agent), CALM, PANIC)
    return DONT_MOVE


panic_grps = {
    CALM: {
        "grp_action": None,
        "mbr_action": agent_action,
        "num_mbrs": DEF_NUM_CALM,
        "color": GREEN
    },
    PANIC: {
        "grp_action": None,
        "mbr_action": agent_action,
        "num_mbrs": DEF_NUM_PANIC,
        "color": RED
    },
}


class Panic(Model):
    def handle_props(self, props):
        super().handle_props(props)
        grid_height = self.props.get("grid_height")
        grid_width = self.props.get("grid_width")
        num_agents = grid_height * grid_width
        pct_panic = self.props.get("pct_panic") / 100
        pct_calm = 1 - pct_panic
        self.grp_struct[CALM]["num_mbrs"] = int(pct_calm * num_agents)
        self.grp_struct[PANIC]["num_mbrs"] = int(pct_panic * num_agents)


def create_model(serial_obj=None):
    """
    This is for the sake of the API server:
    """
    if serial_obj is not None:
        return Panic(serial_obj=serial_obj)
    else:
        return Panic(MODEL_NAME, grp_struct=panic_grps)


def main():
    model = create_model()
    model.run()
    return 0


if __name__ == "__main__":
    main()
