from AirData import AirData
from Vector3 import Vector3

class Air:
    def __init__(self, data: AirData):
        self._density = data.get("density") or 1.225
        self._temperature = data.get("temperature") or 30.0
        self._airArea = data.get("airArea") or Vector3(3000, 3000, 3000)
        self._airWindForce = data.get("airWindForce") or 5.0
        self._airWindDirection = data.get("airWindDirection") or Vector3(0, 0, 0)
