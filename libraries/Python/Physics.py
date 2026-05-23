# Copyright 2026 bananakitssu
# Licensed under the Apache License, Version 2.0

import time
from MathPhysics import MathPhysics
from Workspace import Workspace

class Physics:

    @staticmethod
    def step(workspace: Workspace, delta_time: float):
        """
        Runs one frame of physics simulation on all objects in the workspace.
        Called every frame by BananaPhysics.py
        """
        for uuid, obj in workspace.Objects.items():
            # Skip removed objects
            if obj is None:
                continue

            # Apply gravity
            MathPhysics.apply_gravity(obj, workspace)

            # Apply air resistance and wind for each air zone
            for air in workspace.Airs:
                MathPhysics.apply_air_resistance(obj, air)
                MathPhysics.apply_wind(obj, air)

            # Update position and velocity
            MathPhysics.update_position(obj, delta_time)

