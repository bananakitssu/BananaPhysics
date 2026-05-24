# Copyright 2026 bananakitssu
# Licensed under the Apache License, Version 2.0

import threading
import time
from Physics import Physics
from Workspace import Workspace
from Object import Object
from Air import Air
from Spring import Spring
from String import String
from ObjectConnection import ObjectConnection
from Rubber import Rubber

TICKS_PER_SECOND = 60

def setFPS (fps: int):
    TICKS_PER_SECOND = fps

def LoadWorkspace(workspace: Workspace):
    """
    Starts the physics simulation loop in a background thread.
    Call this once with your workspace and the engine will run automatically.
    
    Example:
        from BananaPhysics import Object, Air, Workspace, LoadWorkspace

        workspace = Workspace({
            "Gravity": 9.8,
        })

        box = Object({
            "Position": Vector3(0, 10, 0),
            "Mass": 5.0,
            "Restitution": 0.7,
        })

        workspace.add(box)
        LoadWorkspace(workspace)
    """
    def loop():
        delta_time = 1.0 / TICKS_PER_SECOND
        while True:
            Physics.step(workspace, delta_time)
            time.sleep(delta_time)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()

