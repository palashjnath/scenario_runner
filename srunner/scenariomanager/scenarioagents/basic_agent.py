#!/usr/bin/env python

# Copyright (c) 2020 Intel Corporation
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.


class BasicAgent(object):

    _actor = None
    _waypoints = []
    _waypoints_updated = False
    _target_speed = 0
    _reached_goal = False
    _init_speed = False
    
    _last_longitudinal_command = None
    _last_lateral_command = None
    _last_waypoint_command = None

    def __init__(self, actor):
        self._actor = actor

    def update_target_speed(self, speed, start_time=None):
        self._target_speed = speed
        self._init_speed = False
        if start_time:
            self._last_longitudinal_command = start_time
    
    def update_waypoints(self, waypoints, start_time=None):
        self._waypoints = waypoints
        self._waypoints_updated = True
        if start_time:
            self._last_waypoint_command = start_time

    def set_init_speed(self):
        self._init_speed = True
        
    def get_last_longitudinal_command(self):
        return self._last_longitudinal_command

    def get_last_waypoint_command(self):
        return self._last_waypoint_command
    
    def check_reached_waypoint_goal(self):
        return self._reached_goal

    def reset(self):
        """
        Pure virtual function to setup user-defined scenario behavior
        """
        raise NotImplementedError(
            "This function is re-implemented by all scenarios"
            "If this error becomes visible the class hierarchy is somehow broken")

    def run_step(self):
        """
        Pure virtual function to setup user-defined scenario behavior
        """
        raise NotImplementedError(
            "This function is re-implemented by all scenarios"
            "If this error becomes visible the class hierarchy is somehow broken")
