# AutonomousVehicleSimulation
Simulating autonomous vehicles using the FLOW library in python

## Overview
The purpose of this project was to create a model which develops autonomous vehicle driving policies using a deep reinforcement learning policy. See [my discussion](https://www.youtube.com/watch?v=qXuBEs9G7Iw&t=12s) or the slide deck in the repo which goes over the general framework and the tools used.

This project was developed using FLOW, to recreate the results see their [readthedocs profile on how to set up the environment](https://flow.readthedocs.io/en/latest/flow_setup.html), merge the files from this repo and use the /flow/experiments/train.py file (or flow/experiments/train_w_7_cores.py for 8 core+ computers) to run any of the minicity examples in this repo. Check back shortly for an ipython notebook which will walk through the process.

## Architecture of the Project

For this project 20 cars using the IDM (intelligent Driver Model) which mimic the acceleration of human drivers were placed in the FLOW minicity environment, cars were added until the average vehicle speed in the system dropped by 50% with 140 human driven cars. After that several different models were made where a portion of the human modeled drivers were replaced with a keras neural network trained using RLlib to address the reduction in speed.

## Credits

[FLOW](https://github.com/flow-project/flow)

[RLlib](https://github.com/ray-project/ray/blob/master/python/ray/rllib)

[SUMO](https://github.com/eclipse/sumo)

[OpenAI Gym](https://github.com/openai/gym)
