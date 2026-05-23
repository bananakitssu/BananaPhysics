from WorkspaceData import WorkspaceData
from Air import Air
from Object import Object
from typing import List

class Workspace:
    def __init__(self, data: WorkspaceData = {}):
        self._gravity = data.get("gravity") or 1.75
        self._air = data.get("Airs") or []
        self._objects = data.get("Objects") or {}
        self._next_id = 0
        
    def add (self, obj: Object):
        uuid = self._next_id
        self._objects[uuid] = obj
        self._next_id += 1
        return uuid
        
    def remove (self, objUuid: int):
        self._objects[objUuid] = None
        
    @property
    def Objects (self):
        return self._objects
        
    @Objects.setter
    def Objects (self, new_objects: List[Object]):
        self._objects = new_objects
        
    @property
    def Airs (self):
        return self._air
        
    @Airs.setter
    def Airs (self, new_air: List[Air]):
        self._air = new_air
        
    @property
    def Gravity (self):
        return self._gravity
        
    @Gravity.setter
    def Gravity (self, new_gravity: float):
        self._gravity = new_gravity
