# Copyright 2026 bananakitssu
# Licensed under the Apache License, Version 2.0

from Vector3 import Vector3

class Rubber:
    def __init__(self, obj, stiffness: float = 20.0, damping: float = 0.1):
        """
        Attaches rubber/trampoline behaviour to an object.
        When something lands on it, it compresses and springs back,
        launching the object upward with more force than a normal bounce.

        obj        -- the object that acts as the rubber surface (e.g. trampoline)
        stiffness  -- how strong the spring back is (higher = more launch force)
        damping    -- how much energy is lost per bounce (lower = bouncier)
        """
        self.obj = obj
        self.stiffness = stiffness
        self.damping = damping

        self._compression = 0.0

        self._rest_y = obj.Position.y

    def impact(self, other):
        """
        Call this when another object lands on the rubber surface.
        Calculates compression based on the landing object's mass and velocity.
        """
        impact_force = other.Mass * abs(other.Velocity.y)

        self._compression = impact_force / self.stiffness

        if not self.obj.Anchored:
            self.obj.Position = Vector3(
                self.obj.Position.x,
                self._rest_y - self._compression,
                self.obj.Position.z
            )

    def step(self, other):
        """
        Every frame, springs back toward rest position and launches the other object.
        Call this every frame while an object is on the rubber surface.
        """
        if self._compression <= 0:
            return

        spring_force = self.stiffness * self._compression

        if not other.Anchored:
            other.Acceleration = other.Acceleration + Vector3(0, spring_force / other.Mass, 0)

        self._compression -= self._compression * self.damping

        if self._compression < 0.01:
            self._compression = 0.0
            if not self.obj.Anchored:
                self.obj.Position = Vector3(
                    self.obj.Position.x,
                    self._rest_y,
                    self.obj.Position.z
                )

