import indra.prop_args2 as props
import os

MODEL_NM = "sim_interactive"

# number of cars
# slow car speed
# acceleration
# deceleration


def run(prop_dict=None):
    pa = props.PropArgs.create_props(MODEL_NM, prop_dict)

    import indra.utils as utils
    import models.sim_interactive as sm

    # set up some file names:
    (prog_file, log_file, prop_file, results_file) = utils.gen_file_names(MODEL_NM)

    (prog_file, log_file, prop_file,
     results_file) = utils.gen_file_names(MODEL_NM)
    # We store basic parameters in a "property" file; this allows us to save
    #  multiple parameter sets, which is important in simulation work.
    #  We can read these in from file or set them here.
    
    if pa["user_type"] == props.WEB:
        pa["base_dir"] = os.environ['base_dir']

    pa["grid_width"] = 20
    pa["grid_height"] = 20
    # print(pa)
    # Now we create an environment for our agents to act within:
    env = sm.SimInteractiveEnv("Car_sim",
                      pa["grid_width"],
                      pa["grid_height"],
                      model_nm=MODEL_NM,
                      props=pa)

    # create given number of slow vehicles
    # print(sm)
    print(env)
    for i in range(pa["slow_car_num"]):
        env.add_agent(sm.Slow('Slow Vehicle #' + str(i)))

    for i in range(pa["fast_car_num"]):
        env.add_agent(sm.Fast('Fast Vehicle #' + str(i)))

    return utils.run_model(env, prog_file, results_file)

if __name__ == "__main__":
    run()