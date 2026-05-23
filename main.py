# Copyright 2026 bananakitssu
# Licensed under the Apache License, Version 2.0

from pathlib import Path
import sys
import time
import threading
import turtle
import BTDPE

current_dir = Path(__file__).resolve().parent
target_dir = current_dir / "libraries" / "Python"
sys.path.append(str(target_dir))
import Object

def run():
    from BananaPhysics import Object, Air, Workspace, LoadWorkspace
    from Vector3 import Vector3

    workspace = Workspace({
        "Gravity": 9.8
    })

    air = Air({
        "Density": 1.225,
        "AirWindForce": 0.0,
        "AirWindDirection": Vector3(0, 0, 0)
    })

    workspace.Airs.append(air)

    box = Object({
        "Position": Vector3(0, 10, 0),
        "Mass": 5.0,
        "Restitution": 0.7,
        "Friction": 0.5
    })

    box_id = workspace.add(box)

    LoadWorkspace(workspace)

    BTDPE_R = threading.Thread(
        target = BTDPE.register_turtle,
        args = (turtle,),
        daemon=True
    )
    BTDPE.registered_meshes = {}
    BTDPE.meshes = {}
    BTDPE.CamX = 0
    BTDPE.CamY = 3
    BTDPE.CamZ = 5
    BTDPE.create_mesh("cube", box_id, {"x": 0, "y": 0, "z": 0}, {"x": 1, "y": 1, "z": 1}, {"x": 0, "y": 0, "z": 0}, False, [], "", False, False, [], {"r": 0, "g": 0, "b": 0}, {"canTransparent": False, "visible": True, "opacity": 1}, [])
    BTDPE_R.start()
    
    while True:
        newBoxPosition = workspace.Objects[box_id].Position
        BTDPE.meshes[box_id]["mesh_position"]["x"] = newBoxPosition["x"]
        BTDPE.meshes[box_id]["mesh_position"]["y"] = newBoxPosition["y"]
        BTDPE.meshes[box_id]["mesh_position"]["z"] = newBoxPosition["z"]
        time.sleep(1/60)
