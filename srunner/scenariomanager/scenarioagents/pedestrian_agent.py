#!/usr/bin/env python

# Copyright (c) 2018-2020 Intel Corporation
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.


import math

from srunner.scenariomanager.scenarioagents.basic_agent import BasicAgent


class PedestrianAgent(BasicAgent):
    
    def __init__(self, actor):
        super(PedestrianAgent, self).__init__(actor)

    def reset(self):

        if self._actor and self._actor.is_alive:
            self._actor = None

    def run_step(self):
        
        if not self._actor or not self._actor.is_alive:
            return

        control = self._actor.get_control()
        control.speed = self._target_speed

        if self._waypoints:
            self._reached_goal = False
            location = self._waypoints[0].transform.location
            direction = location - self._actor.get_location()
            direction_norm = math.sqrt(direction.x**2 + direction.y**2)
            control.direction = direction / direction_norm
            self._actor.apply_control(control)
            if direction_norm < 1.0:
                self._waypoints = self._waypoints[1:]
                if not self._waypoints:
                    self._reached_goal = True
        else:
            control.direction = self._actor.get_transform().rotation.get_forward_vector()
            self._actor.apply_control(control)
