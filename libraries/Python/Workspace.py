from WorkspaceData import WorkspaceData
from Air import Air
from Object import Object
from Spring import Spring
from String import String
from ObjectConnection import ObjectConnection
from Rubber import Rubber
from typing import List

class Workspace:
    def __init__(self, data: WorkspaceData = {}):
        self._gravity = data.get("Gravity") or 1.75
        self._air = data.get("Airs") or []
        self._objects = data.get("Objects") or {}
        self._next_id = 0
        self._springs = data.get("Springs") or []
        self._strings = data.get("Strings") or []
        self._connections = data.get("Connections") or []
        self._rubbers = data.get("Rubbers") or []
        
    def add (self, obj: Object):
        uuid = self._next_id
        obj.uuid = uuid
        self._objects[uuid] = obj
        self._next_id += 1
        return uuid
        
    def add_spring(self, spring):
        self._springs.append(spring)
        return spring
        
    def add_string(self, string):
        self._strings.append(string)
        return string
        
    def add_connection(self, objectConnection):
        self._connections.append(objectConnection)
        return objectConnection
        
    def add_rubber (self, rubber):
        self._rubbers.append(rubber)
        return rubber
        
    def remove (self, objUuid: int):
        self._objects[objUuid] = None
        
    @property
    def Objects (self):
        return self._objects
        
    @property
    def Connections (self):
        return self._connections
        
    @property
    def Strings (self):
        return self._strings
        
    @property
    def Rubbers (self):
        return self._rubbers
        
    @property
    def Springs (self):
        return self._springs
        
    @Objects.setter
    def Objects (self, new_objects: List[Object]):
        self._objects = new_objects
        
    @Connections.setter
    def Connections (self, new_connections: List[ObjectConnection]):
        self._connections = new_connections
        
    @Strings.setter
    def Strings (self, new_strings: List[String]):
        self._strings = new_strings
        
    @Rubbers.setter
    def Rubbers (self, new_rubbers: List[Rubber]):
        self._rubbers = new_rubbers
        
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
