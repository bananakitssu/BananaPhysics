from Vector3 import Vector3
from ObjectData import ObjectData

class Object:
    def __init__ (self, data: ObjectData = {}):
        self._position = data.get("Position") or Vector3(0, 0, 0)
        self._rotation = data.get("Rotation") or Vector3(0, 0, 0)
        self._acceleration = data.get("Acceleration") or Vector3(0, 0, 0)
        self._friction = data.get("Friction") or 0.5
        self._restitution = data.get("Restitution") or 0.7
        self._mass = data.get("Mass") or 1.0
        self._velocity = data.get("Velocity") or Vector3(0, 0, 0)
        self._size = data.get("Size") or Vector3(1, 1, 1)
        self._anchored = data.get("Anchored") or False
        self._uuid = 0
        
        self.edges = [
            Vector3(-self._size.x,  self._size.y,  self._size.z),
            Vector3(-self._size.x,  self._size.y, -self._size.z),
            Vector3( self._size.x,  self._size.y, -self._size.z),
            Vector3( self._size.x,  self._size.y,  self._size.z),
            Vector3( self._size.x, -self._size.y,  self._size.z),
            Vector3(-self._size.x, -self._size.y,  self._size.z),
            Vector3(-self._size.x, -self._size.y, -self._size.z),
            Vector3( self._size.x, -self._size.y, -self._size.z)
        ]
        
    @property
    def uuid (self):
        return self._uuid
        
    @uuid.setter
    def uuid (self, new_uuid):
        self._uuid = new_uuid
        
    @property
    def Anchored (self):
        return self._anchored
        
    @Anchored.setter
    def Anchored (self, new_bool: bool):
        self._anchored = new_bool
        
    @property
    def Size (self):
        return self._size
        
    @Size.setter
    def Size (self, new_size: Vector3):
        self._size = new_size
        self._update_edges()
        
    @property
    def Position (self):
        return self._position
        
    @Position.setter
    def Position (self, new_position: Vector3):
        self._position = new_position
        
    @property
    def Rotation (self):
        return self._rotation
        
    @Rotation.setter
    def Rotation(self, new_rotation: Vector3):
        self._rotation = new_rotation
        
    @property
    def Restitution(self):
        return self._restitution
        
    @Restitution.setter
    def Restitution(self, new_restitution: float):
        self._restitution = new_restitution
        
    @property
    def Mass (self):
        return self._mass
        
    @Mass.setter
    def Mass (self, new_mass: float):
        self._mass = new_mass
        
    @property
    def Velocity (self):
        return self._velocity
        
    @Velocity.setter
    def Velocity (self, new_velocity: Vector3):
        self._velocity = new_velocity
        
    @property
    def Acceleration (self):
        return self._acceleration
        
    @Acceleration.setter
    def Acceleration (self, new_acceleration: Vector3):
        self._acceleration = new_acceleration
        
    @property
    def Friction(self):
        return self._friction
        
    @Friction.setter
    def Friction(self, new_friction: float):
        self._friction = new_friction
        
    @property
    def Edges(self):
        return self.edges
        
    def _update_edges (self):
        s = self._size
        self.edges = [
            Vector3(-s.x,  s.y,  s.z),
            Vector3(-s.x,  s.y, -s.z),
            Vector3( s.x,  s.y, -s.z),
            Vector3( s.x,  s.y,  s.z),
            Vector3( s.x, -s.y,  s.z),
            Vector3(-s.x, -s.y,  s.z),
            Vector3(-s.x, -s.y, -s.z),
            Vector3( s.x, -s.y, -s.z)
        ]
