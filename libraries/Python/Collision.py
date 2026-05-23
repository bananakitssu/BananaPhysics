# Copyright 2026 bananakitssu
# Licensed under the Apache License, Version 2.0

from Vector3 import Vector3
from MathPhysics import MathPhysics

class Collision:

    @staticmethod
    def check(objA, objB):
        """
        Checks if two objects are overlapping using AABB.
        Returns True if they are colliding, False if not.
        """
        aMin = Vector3(
            objA.Position.x - objA.Size.x / 2,
            objA.Position.y - objA.Size.y / 2,
            objA.Position.z - objA.Size.z / 2
        )
        aMax = Vector3(
            objA.Position.x + objA.Size.x / 2,
            objA.Position.y + objA.Size.y / 2,
            objA.Position.z + objA.Size.z / 2
        )

        bMin = Vector3(
            objB.Position.x - objB.Size.x / 2,
            objB.Position.y - objB.Size.y / 2,
            objB.Position.z - objB.Size.z / 2
        )
        bMax = Vector3(
            objB.Position.x + objB.Size.x / 2,
            objB.Position.y + objB.Size.y / 2,
            objB.Position.z + objB.Size.z / 2
        )
        
        return (
            aMin.x <= bMax.x and aMax.x >= bMin.x and
            aMin.y <= bMax.y and aMax.y >= bMin.y and
            aMin.z <= bMax.z and aMax.z >= bMin.z
        )

    @staticmethod
    def get_normal(objA, objB):
        """
        Figures out which face of objB was hit by objA.
        Returns the surface normal (direction to bounce off).
        """
        diff = objA.Position - objB.Position

        overlapX = (objA.Size.x + objB.Size.x) / 2 - abs(diff.x)
        overlapY = (objA.Size.y + objB.Size.y) / 2 - abs(diff.y)
        overlapZ = (objA.Size.z + objB.Size.z) / 2 - abs(diff.z)

        if overlapX < overlapY and overlapX < overlapZ:
            return Vector3(1 if diff.x > 0 else -1, 0, 0)
        elif overlapY < overlapX and overlapY < overlapZ:
            return Vector3(0, 1 if diff.y > 0 else -1, 0)
        else:
            return Vector3(0, 0, 1 if diff.z > 0 else -1)

    @staticmethod
    def resolve(objA, objB):
        """
        Resolves collision between two objects.
        - If both are anchored, do nothing
        - If one is anchored, only the other one bounces
        - If neither is anchored, both bounce off each other
        """
        if objA.Anchored and objB.Anchored:
            return

        normal = Collision.get_normal(objA, objB)

        if objA.Anchored:
            MathPhysics.resolve_bounce(objB, -normal)
            MathPhysics.apply_friction(objB)
            Collision._push_out(objB, objA, -normal)

        elif objB.Anchored:
            MathPhysics.resolve_bounce(objA, normal)
            MathPhysics.apply_friction(objA)
            Collision._push_out(objA, objB, normal)

        else:
            totalMass = objA.Mass + objB.Mass

            ratioA = objB.Mass / totalMass
            ratioB = objA.Mass / totalMass

            velocityA = objA.Velocity
            velocityB = objB.Velocity

            restitution = (objA.Restitution + objB.Restitution) / 2
            objA.Velocity = velocityB * ratioA * restitution + velocityA * (1 - ratioA)
            objB.Velocity = velocityA * ratioB * restitution + velocityB * (1 - ratioB)

            MathPhysics.apply_friction(objA)
            MathPhysics.apply_friction(objB)

            Collision._push_out(objA, objB, normal)

    @staticmethod
    def _push_out(moving, stationary, normal):
        """
        Pushes the moving object out of the stationary one so they don't overlap.
        Without this, objects sink into each other.
        """
        overlapX = (moving.Size.x + stationary.Size.x) / 2 - abs(moving.Position.x - stationary.Position.x)
        overlapY = (moving.Size.y + stationary.Size.y) / 2 - abs(moving.Position.y - stationary.Position.y)
        overlapZ = (moving.Size.z + stationary.Size.z) / 2 - abs(moving.Position.z - stationary.Position.z)

        moving.Position = Vector3(
            moving.Position.x + normal.x * overlapX,
            moving.Position.y + normal.y * overlapY,
            moving.Position.z + normal.z * overlapZ
        )

