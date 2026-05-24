# Copyright 2026 bananakitssu
# Licensed under the Apache License, Version 2.0

from Vector3 import Vector3

class ObjectConnection:
    def __init__(self, objectA, objectB):
        """
        Welds two objects together so they move as one.
        objectA -- the main object (the one that leads)
        objectB -- the object that follows objectA
        
        The offset between them is recorded at connection time
        and maintained every frame.
        """
        self.objectA = objectA
        self.objectB = objectB

        self.offset = objectB.Position - objectA.Position

    def step(self):
        """
        Forces objectB to maintain its offset from objectA every frame.
        objectB copies objectA's velocity so they move together.
        """
        if self.objectA.Anchored and self.objectB.Anchored:
            return

        self.objectB.Position = self.objectA.Position + self.offset

        self.objectB.Velocity = self.objectA.Velocity.copy()

        self.objectB.Acceleration = self.objectA.Acceleration.copy()

