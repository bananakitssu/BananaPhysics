from typing import TypedDict, Optional
from Vector3 import Vector3

class AirData(TypedDict, total=False):
    airArea: Vector3
    airWindDirection: Vector3
    airForce: float
    density: float
    temperature: float
