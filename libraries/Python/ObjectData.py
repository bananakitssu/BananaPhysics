from typing import TypedDict, Optional
from Vector3 import Vector3

class ObjectData(TypedDict, total=False):
    position: Vector3
    velocity: Vector3
    mass: float
    restitution: float
    friction: float
    acceleration: Vector3
    rotation: Vector3
    size: Vector3
