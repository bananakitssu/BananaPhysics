from typing import TypedDict, Optional, List
from Vector3 import Vector3
from Object import Object
from Air import Air
from Spring import Spring
from String import String

class WorkspaceData(TypedDict, total=False):
    Objects: List[Object]
    Airs: List[Air]
    Springs: List[Spring]
    Strings: List[String]
    Gravity: float
