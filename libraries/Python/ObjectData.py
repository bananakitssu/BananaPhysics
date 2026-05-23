from typing import TypedDict, Optional
from Vector3 import Vector3

class ObjectData(TypedDict, total=False):
    Position: Vector3
    Velocity: Vector3
    Mass: float
    Restitution: float
    Friction: float
    Acceleration: Vector3
    Rotation: Vector3
    Size: Vector3
    Anchored: bool
