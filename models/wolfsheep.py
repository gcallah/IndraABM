from lib.agent import MOVE, DONT_MOVE
from lib.display_methods import TAN, GRAY
from lib.model import Model, NUM_MBRS, MBR_ACTION, NUM_MBRS_PROP, COLOR
from lib.utils import Debug
from lib.space import get_num_of_neighbors, get_neighbor

MODEL_NAME = "wolfsheep"

NUM_WOLVES = 8
NUM_SHEEP = 28
PREY_DIST = 3
TOO_CROWDED = 6
CROWDING_EFFECT = 1
MAX_ENERGY = 3
MEADOW_HEIGHT = 10
MEADOW_WIDTH = 10

WOLF_LIFESPAN = 5
WOLF_REPRO_PERIOD = 2

SHEEP_LIFESPAN = 8
SHEEP_REPRO_PERIOD = 2


def sheep_action(agent, **kwargs):

    # Die if the agent runs out of duration
    if agent.duration <= 0:
        agent.die()
        return DONT_MOVE

    # Initialize the attribute
    if agent.get_attr("ttr") is None:
        agent.set_attr("ttr", 10)

    # Decrease ttr
    agent.set_attr("ttr", agent.get_attr("ttr") - 1)

    # Check neighbor count
    if get_num_of_neighbors(agent, size=10) > TOO_CROWDED:
        agent.duration -= CROWDING_EFFECT

    # Check if it is time to produce
    if agent.get_attr("ttr") == 0:
        # reproduce function
        print("Time to produce!")

    return MOVE


def wolf_action(agent, **kwargs):

    prey = get_neighbor(agent=agent, size=3)

    if prey is not None:
        if Debug().debug:
            print(str(agent) + " is eating " + str(prey))

        agent.duration += min(prey.duration, MAX_ENERGY)
        prey.die()

    else:
        agent.duration /= 2

    # Die if the agent runs out of duration
    if agent.duration <= 0:
        agent.die()
        return DONT_MOVE

    # Initialize the attribute
    if agent.get_attr("ttr") is None:
        agent.set_attr("ttr", 10)

    # Decrease ttr
    agent.set_attr("ttr", agent.get_attr("ttr") - 1)

    # Check if it is time to produce
    if agent.get_attr("ttr") == 0:
        # reproduce function
        print("Time to produce!")


basic_grps = {
    "sheep_": {
        MBR_ACTION: sheep_action,
        NUM_MBRS: NUM_SHEEP,
        NUM_MBRS_PROP: "num_sheep",
        COLOR: GRAY,
    },
    "wolf_": {
        MBR_ACTION: wolf_action,
        NUM_MBRS: NUM_WOLVES,
        NUM_MBRS_PROP: "num_wolves",
        COLOR: TAN,
    },
}


class WolfSheep(Model):
    """
    This class should just create a basic model that runs, has
    some agents that move around, and allows us to test if
    the system as a whole is working.
    It turns out that so far, we don't really need to subclass anything!
    """


def create_model(serial_obj=None, props=None):
    """
    This is for the sake of the API server:
    """
    if serial_obj is not None:
        return WolfSheep(serial_obj=serial_obj)
    else:
        return WolfSheep(MODEL_NAME, grp_struct=basic_grps, props=props)


def main():
    model = create_model()
    model.run()

    return 0


if __name__ == "__main__":
    main()
