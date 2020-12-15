# AutonomousVehicleSimulation
Modelling and simulating autonomous vehicles using the FLOW library in python

## Overview
The purpose of this project was to create a model which develops autonomous vehicle driving policies using a deep reinforcement learning policy. See [my discussion](https://www.youtube.com/watch?v=qXuBEs9G7Iw&t=12s) or the slide deck in the repo which goes over the general framework and the tools used.

This project was developed using FLOW, to recreate the results see their [readthedocs profile on how to set up the environment](https://flow.readthedocs.io/en/latest/flow_setup.html), merge the files from this repo and use the /flow/experiments/train.py file (or flow/experiments/train_w_7_cores.py for 8 core+ computers) to run any of the minicity examples in this repo. Check back shortly for an ipython notebook which will walk through the process.

## Architecture of the Project

For this project 20 cars using the IDM (intelligent Driver Model) which mimic the acceleration of human drivers were placed in the FLOW minicity environment, cars were added until the average vehicle speed in the system dropped by 50% with 140 human driven cars. After that several different models were made where a portion of the human modeled drivers were replaced with a keras neural network trained using RLlib to address the reduction in speed. This neural network took the speed and location of the car as well as the speed and distances of the cars directly infront of and behind it to determine acceleration/deceleration for the vehicle. This policy was shared among all of the RL vehicles and the reward was based on the speed of all the vehicles in the system.

![RL Acceleration Model](https://github.com/rlew631/AutonomousVehicleSimulation/blob/main/RL%20diagram.png?raw=true)

## The Models

| Model           | Description |
|-----------------|------------------|
| ma2_minicity.py | Replaces 5% of the IDM drivers in the system with vehicles using an RL based acceleration policy |
| ma_minicity_noise_10p.py | Replaces 10% of the IDM drivers and added 0.2 standard deviations of noise to the NN input |
| ma_minicity_noise_20p.py | Replaces 20% of the IDM drivers |
| ma_minicity_noise_30p.py | Replaces 30% of the IDM drivers |
| ma_minicity_noise_and_penalty.py | Implemented RyanAccelPOEnv which adds a penalty for ending the simulation early |

To see a demo of the `ma_minicity_noise_20p` experiment in a jupyter notebook take a look at the MultiAgent_MiniCity_Demo.ipynb file. This is best viewed locally since the experiment output for each step in the simulation is shown in the file when viewing in github. To see the plotted results and some discussion simply scroll to the bottom of the file.

## Credits

[FLOW](https://github.com/flow-project/flow)

[RLlib](https://github.com/ray-project/ray/blob/master/python/ray/rllib)

[SUMO](https://github.com/eclipse/sumo)

[OpenAI Gym](https://github.com/openai/gym)
