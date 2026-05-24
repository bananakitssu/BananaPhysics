# Copyright 2026 bananakitssu
# Licensed under the Apache License, Version 2.0

from Vector3 import Vector3

class String:
    def __init__(self, objectA, objectB, stiffness: float = 10.0, rest_length: float = 1.0, damping: float = 0.5):
        """
        A string connecting two objects.
        
        objectA, objectB -- the two objects connected by the spring
        stiffness        -- how strong the spring is (higher = stiffer, snaps back faster)
        rest_length      -- the natural length of the spring when not stretched or compressed
        damping          -- how fast the spring loses energy (0 = bounces forever, 1 = no bounce)
        """
        self.objectA = objectA
        self.objectB = objectB
        self.stiffness = stiffness
        self.rest_length = rest_length
        self.damping = damping

    def step(self):
        """
        Applies string forces to both objects every frame.
        Uses Hooke's Law: F = -stiffness * (current_length - rest_length)
        """
        diff = self.objectB.Position - self.objectA.Position
        current_length = diff.magnitude()

        if current_length == 0:
            return

        stretch = current_length - self.rest_length
        
        if stretch <= 0:
            return

        direction = diff.normalize()

        spring_force = direction * (self.stiffness * stretch)

        relative_velocity = self.objectB.Velocity - self.objectA.Velocity
        damping_force = direction * (self.damping * relative_velocity.dot(direction))

        total_force = spring_force + damping_force

        if not self.objectA.Anchored:
            self.objectA.Acceleration = self.objectA.Acceleration + total_force / self.objectA.Mass

        if not self.objectB.Anchored:
            self.objectB.Acceleration = self.objectB.Acceleration - total_force / self.objectB.Mass

