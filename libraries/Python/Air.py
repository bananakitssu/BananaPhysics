from AirData import AirData
from Vector3 import Vector3

class Air:
    def __init__(self, data: AirData = {}):
        self._density = data.get("Density") or 1.225
        self._temperature = data.get("Temperature") or 30.0
        self._airArea = data.get("AirArea") or Vector3(3000, 3000, 3000)
        self._airWindForce = data.get("AirWindForce") or 5.0
        self._airWindDirection = data.get("AirWindDirection") or Vector3(0, 0, 0)
        
    @property
    def Density(self):
        return self._density

    @Density.setter
    def Density(self, value: float):
        self._density = value

    @property
    def Temperature(self):
        return self._temperature

    @Temperature.setter
    def Temperature(self, value: float):
        self._temperature = value

    @property
    def AirArea(self):
        return self._airArea

    @AirArea.setter
    def AirArea(self, value: Vector3):
        self._airArea = value

    @property
    def AirWindForce(self):
        return self._airWindForce

    @AirWindForce.setter
    def AirWindForce(self, value: float):
        self._airWindForce = value

    @property
    def AirWindDirection(self):
        return self._airWindDirection

    @AirWindDirection.setter
    def AirWindDirection(self, value: Vector3):
        self._airWindDirection = value
