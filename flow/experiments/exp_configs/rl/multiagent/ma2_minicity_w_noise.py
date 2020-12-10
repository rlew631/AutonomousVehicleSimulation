"""Example of modified minicity network with human-driven vehicles."""
import random
import numpy as np
import os

from flow.controllers.base_routing_controller import BaseRouter

from flow.controllers import IDMController
from flow.controllers import RLController
from flow.core.params import SumoParams, EnvParams, NetParams, InitialConfig
from flow.core.params import SumoCarFollowingParams, SumoLaneChangeParams
from flow.core.params import VehicleParams
#from flow.envs.ring.accel import AccelEnv, ADDITIONAL_ENV_PARAMS
from flow.envs.multiagent.minicity import MultiAgentAccelPOEnv, ADDITIONAL_ENV_PARAMS
from flow.controllers.routing_controllers import MinicityRouter
from flow.networks.minicity import MiniCityNetwork



# number of rollouts per training iteration
N_ROLLOUTS = 20
# number of parallel workers
N_CPUS = 2

vehicles = VehicleParams()
total_num_vehicles = 140
percent_autonomous = 5 #use increments of 5%
num_autonomous = int(total_num_vehicles - (total_num_vehicles*percent_autonomous)/100)
num_humans = total_num_vehicles - num_autonomous
vehicles.add(
    veh_id="idm",
    acceleration_controller=(IDMController, {"noise": 0.2}),
    routing_controller=(MinicityRouter, {}),
    car_following_params=SumoCarFollowingParams(
        speed_mode=1,
    ),
    lane_change_params=SumoLaneChangeParams(
        lane_change_mode="no_lc_safe",
    ),
    initial_speed=0,
    num_vehicles=num_humans)
    #num_vehicles=50)
vehicles.add(
    veh_id="rl",
    acceleration_controller=(RLController, {}),
    routing_controller=(MinicityRouter, {}),
    car_following_params=SumoCarFollowingParams(
        speed_mode="obey_safe_speed",
    ),
    initial_speed=0,
    #num_vehicles=3)
    num_vehicles=num_autonomous)


flow_params = dict(
    # name of the experiment
    exp_tag='minicity',

    # name of the flow environment the experiment is running on
    env_name=MultiAgentAccelPOEnv,

    # name of the network class the experiment is running on
    network=MiniCityNetwork,

    # simulator that is used by the experiment
    simulator='traci',

    # sumo-related parameters (see flow.core.params.SumoParams)
    sim=SumoParams(
        sim_step=0.25,
        render=False,
	restart_instance=True
#        render='drgb',
#        save_render=False,
#        sight_radius=30,
#        pxpm=3,
#        show_radius=True,
    ),

    # environment related parameters (see flow.core.params.EnvParams)
    env=EnvParams(
        horizon=2000,
	warmup_steps=100,
        additional_params=ADDITIONAL_ENV_PARAMS
    ),

    # network-related parameters (see flow.core.params.NetParams and the
    # network's documentation or ADDITIONAL_NET_PARAMS component)
    net=NetParams(),

    # vehicles to be placed in the network at the start of a rollout (see
    # flow.core.params.VehicleParams)
    veh=vehicles,

    # parameters specifying the positioning of vehicles upon initialization/
    # reset (see flow.core.params.InitialConfig)
    initial=InitialConfig(
        spacing="random",
        min_gap=5,
    ),
)
