from WorkspaceData import WorkspaceData
from Air import Air
from Object import Object
from Spring import Spring
from typing import List

class Workspace:
    def __init__(self, data: WorkspaceData = {}):
        self._gravity = data.get("Gravity") or 1.75
        self._air = data.get("Airs") or []
        self._objects = data.get("Objects") or {}
        self._next_id = 0
        self._springs = data.get("Springs") or []
        
    def add (self, obj: Object):
        uuid = self._next_id
        obj.uuid = uuid
        self._objects[uuid] = obj
        self._next_id += 1
        return uuid
        
    def add_spring(self, spring):
        self._springs.append(spring)
        return spring
        
    def remove (self, objUuid: int):
        self._objects[objUuid] = None
        
    @property
    def Objects (self):
        return self._objects
        
    @property
    def Springs (self):
        return self._springs
        
    @Objects.setter
    def Objects (self, new_objects: List[Object]):
        self._objects = new_objects
        
    @Springs.setter
    def Springs (self, new_springs: List[Spring]):
        self._springs = new_springs
        
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
