from typing import TypedDict, Optional
from Vector3 import Vector3

class AirData(TypedDict, total=False):
    AirArea: Vector3
    AirWindDirection: Vector3
    AirForce: float
    Density: float
    Temperature: float
