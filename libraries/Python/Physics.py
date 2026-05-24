# Copyright 2026 bananakitssu
# Licensed under the Apache License, Version 2.0

import time
from MathPhysics import MathPhysics
from Workspace import Workspace
from Collision import Collision
from Spring import Spring
from String import String
from ObjectConnection import ObjectConnection
from Rubber import Rubber

class Physics:

    @staticmethod
    def step(workspace: Workspace, delta_time: float):
        """
        Runs one frame of physics simulation on all objects in the workspace.
        Called every frame by BananaPhysics.py
        """
        for uuid, obj in workspace.Objects.items():
            if obj is None:
                continue

            MathPhysics.apply_gravity(obj, workspace)

            for air in workspace.Airs:
                MathPhysics.apply_air_resistance(obj, air)
                MathPhysics.apply_wind(obj, air)

            MathPhysics.update_position(obj, delta_time)

            objects = [obj for obj in workspace.Objects.values() if obj is not None]
    
            for i in range(len(objects)):
                for j in range(i + 1, len(objects)):  # i+1 so we don't check the same pair twice
                    objA = objects[i]
                    objB = objects[j]
            
                    if Collision.check(objA, objB):
                        Collision.resolve(objA, objB)

            for spring in workspace.Springs:
                spring.step()

            for string in workspace.Strings:
                string.step()
                
            for connection in workspace.Connections:
                connection.step()
                
            for rubber in workspace.Rubbers:
                for uuid, obj in workspace.Objects.items():
                    if obj is not None and not obj.Anchored:
                        rubber.step(obj)
