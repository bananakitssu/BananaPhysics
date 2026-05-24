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

def run():
    from BananaPhysics import Object, Air, Spring, Workspace, LoadWorkspace, Rubber
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

    floor = Object({
        "Position": Vector3(0, 0, 0),
        "Size": Vector3(20, 1, 20),
        "Anchored": True,
        "Mass": 1.0,
        "Restitution": 0.7,
        "Friction": 0.5
    })

    floor_id = workspace.add(floor)
    
    trampoline = Object({
        "Position": Vector3(0, 1, 0),
        "Size": Vector3(10, 1, 10),
        "Anchored": True,
        "Restitution": 0.0,
    })

    rubber = Rubber(trampoline, stiffness=25.0, damping=0.1)
    trampoline.Rubber = rubber
    workspace.add_rubber(rubber)
    
    #spring = Spring(box, floor, stiffness=15.0, rest_length=2.0, damping=0.5)
    #workspace.add_spring(spring)

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
    BTDPE.CamZ = 12
    BTDPE.create_mesh(
        "cube",
        floor_id,
        {"x": 0, "y": 0, "z": 0},
        {"x": 20, "y": 1, "z": 20},
        {"x": 0, "y": 0, "z": 0},
        False, [], "", False, False, [],
        {"r": 0, "g": 0, "b": 0},
        {"canTransparent": False, "visible": True, "opacity": 1},
        []
    )
    #BTDPE.create_mesh("cube", box_id, {"x": 0, "y": 0, "z": 0}, {"x": 1, "y": 1, "z": 1}, {"x": 0, "y": 0, "z": 0}, False, [], "", False, False, [], {"r": 0, "g": 0, "b": 0}, {"canTransparent": False, "visible": True, "opacity": 1}, [])
    BTDPE_R.start()
    
    while True:
        for obj in workspace.Objects.values():
            objBTDPE = next((item for item in BTDPE.meshes.values() if item is not None and isinstance(item, dict) and item.get('name') == obj.uuid), None)
            if objBTDPE is None:
                BTDPE.create_mesh(
                    "cube",
                    obj.uuid,
                    {"x": obj.Position.x, "y": obj.Position.y, "z": obj.Position.z},
                    {"x": obj.Size.x, "y": obj.Size.y, "z": obj.Size.z},
                    {"x": 0, "y": 0, "z": 0},
                    False, [], "", False, False, [],
                    {"r": 0, "g": 0, "b": 0},
                    {"canTransparent": False, "visible": True, "opacity": 1},
                    []
                )
            else:
                objBTDPE["mesh_position"]["x"] = obj.Position.x
                objBTDPE["mesh_position"]["y"] = obj.Position.y
                objBTDPE["mesh_position"]["z"] = obj.Position.z
                objBTDPE["mesh_size"]["x"] = obj.Size.x
                objBTDPE["mesh_size"]["y"] = obj.Size.y
                objBTDPE["mesh_size"]["z"] = obj.Size.z
        #newBoxPosition = workspace.Objects[box_id].Position
        #newFloorPosition = workspace.Objects[floor_id].Position
        #BTDPE.meshes[box_id]["mesh_position"]["x"] = newBoxPosition.x
        #BTDPE.meshes[box_id]["mesh_position"]["y"] = newBoxPosition.y
        #BTDPE.meshes[box_id]["mesh_position"]["z"] = newBoxPosition.z
        #BTDPE.meshes[floor_id]["mesh_position"]["x"] = newFloorPosition.x
        #BTDPE.meshes[floor_id]["mesh_position"]["y"] = newFloorPosition.y
        #BTDPE.meshes[floor_id]["mesh_position"]["z"] = newFloorPosition.z
        time.sleep(1/60)
        
run()
