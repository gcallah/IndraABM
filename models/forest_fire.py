
"""
A model for how fires spread through a forest.
"""

from lib.agent import DONT_MOVE
from lib.display_methods import TOMATO, GREEN, RED, SPRINGGREEN, BLACK
from lib.model import Model
from lib.agent import prob_state_trans
from lib.space import exists_neighbor
from registry.registry import get_model

MODEL_NAME = "forest_fire"
DEBUG = False  # turns debugging code on or off
DEBUG2 = False  # turns deeper debugging code on or off

DEF_NUM_TREES = 10
DEF_DIM = 30
DEF_DENSITY = .44
DEF_NEW_FIRE = .01
# tree group names
HEALTHY = "Healthy"
NEW_FIRE = "New Fire"
ON_FIRE = "On Fire"
BURNED_OUT = "Burned Out"
NEW_GROWTH = "New Growth"

# state numbers: create as strings for JSON,
# convert to int when we need 'em that way
HE = "0"
NF = "1"
OF = "2"
BO = "3"
NG = "4"

TRANS_TABLE = "trans_table"
state_trans = [
    [1 - DEF_NEW_FIRE, DEF_NEW_FIRE, 0.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, .99, .01],
    [1.0, 0.0, 0.0, 0.0, 0.0],
]

GROUP_MAP = "group_map"

STATE_MAP = {HEALTHY: HE,
             NEW_FIRE: NF,
             ON_FIRE: OF,
             BURNED_OUT: BO,
             NEW_GROWTH: NG}

GROUP_MAP = {HE: HEALTHY,
             NF: NEW_FIRE,
             OF: ON_FIRE,
             BO: BURNED_OUT,
             NG: NEW_GROWTH}


def tree_action(agent, **kwargs):
    """
    A simple default agent action.
    """
    model = get_model(agent.exec_key)
    old_group = agent.group_name()
    if old_group == HEALTHY:
        if exists_neighbor(agent, lambda agent: agent.group_name() == ON_FIRE):
            if DEBUG2:
                print("Setting nearby tree on fire!")
            model.add_switch(str(agent), HEALTHY, NEW_FIRE)

    # if we didn't catch on fire above, do probabilistic transition:
    if old_group == agent.group_name():
        curr_state = STATE_MAP[old_group]
        # we gotta do these str/int shenanigans with state cause
        # JSON only allows strings as dict keys
        agent.has_acted = True
        agent.set_prim_group(GROUP_MAP[str(prob_state_trans(int(curr_state),
                                                            state_trans))])

        if DEBUG2:
            if agent.group_name == NEW_FIRE:
                print("Tree spontaneously catching fire.")

    if old_group != agent.group_name():
        # if we entered a new state, then...
        agent.has_acted = True
        model.add_switch(str(agent),
                         old_group,
                         agent.group_name())
    return DONT_MOVE


ff_grps = {
    HEALTHY: {
        "mbr_action": tree_action,
        "num_mbrs": DEF_NUM_TREES,
        "color": GREEN,
    },
    NEW_FIRE: {
        "num_mbrs": 0,
        "color": TOMATO,
    },
    ON_FIRE: {
        "num_mbrs": 0,
        "color": RED,
    },
    BURNED_OUT: {
        "num_mbrs": 0,
        "color": BLACK,
    },
    NEW_GROWTH: {
        "num_mbrs": 0,
        "color": SPRINGGREEN,
    },
}


class ForestFire(Model):
    """
    The forest fire model.
    """
    def handle_props(self, props):
        super().handle_props(props)
        height = self.props.get("grid_height")
        width = self.props.get("grid_width")
        density = self.props.get("density")
        num_agents = int(height * width * density)
        self.grp_struct[HEALTHY]["num_mbrs"] = num_agents


def create_model(serial_obj=None):
    """
    This is for the sake of the API server:
    """
    if serial_obj is not None:
        return ForestFire(serial_obj=serial_obj)
    else:
        return ForestFire(MODEL_NAME, grp_struct=ff_grps)


def main():
    model = create_model()
    model.run()
    return 0


if __name__ == "__main__":
    main()
