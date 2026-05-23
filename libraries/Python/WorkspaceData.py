from typing import TypedDict, Optional, List
from Vector3 import Vector3
from Object import Object
from Air import Air

class WorkspaceData(TypedDict, total=False):
    Objects: List[Object]
    Airs: List[Air]
    Gravity: float
