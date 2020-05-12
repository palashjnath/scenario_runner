#!/usr/bin/env python

# Copyright (c) 2018-2020 Intel Corporation
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import importlib
import os
import sys

import carla

from srunner.scenariomanager.scenarioagents.npc_vehicle_agent import NpcVehicleAgent
from srunner.scenariomanager.scenarioagents.pedestrian_agent import PedestrianAgent


class ActorAgent(object):

    def __init__(self, actor, agent, args):

        # use importlib to import agent
        # provide args to agent

        if not agent:
            if isinstance(actor, carla.Walker):
                self.agent_instance = PedestrianAgent(actor)
            else:
                self.agent_instance = NpcVehicleAgent(actor)
        else:
            module_name = os.path.basename(agent).split('.')[0]
            sys.path.insert(0, os.path.dirname(agent))
            self.module_agent = importlib.import_module(module_name)
            agent_class_name = self.module_agent.__name__.title().replace('_', '')
            self.agent_instance = getattr(self.module_agent, agent_class_name)(actor, args)

    def reset(self):
        self.agent_instance.reset()

    def update_target_speed(self, target_speed, start_time=None):
        self.agent_instance.update_target_speed(target_speed, start_time)

    def update_waypoints(self, waypoints, start_time=None):
        self.agent_instance.update_waypoints(waypoints, start_time)

    def check_reached_waypoint_goal(self):
        return self.agent_instance.check_reached_waypoint_goal()

    def get_last_longitudinal_command(self):
        return self.agent_instance.get_last_longitudinal_command()

    def get_last_waypoint_command(self):
        return self.agent_instance.get_last_waypoint_command()

    def set_init_speed(self):
        self.agent_instance.set_init_speed()

    def run_step(self):
        self.agent_instance.run_step()
