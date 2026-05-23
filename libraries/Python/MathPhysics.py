# Copyright 2026 bananakitssu
# Licensed under the Apache License, Version 2.0

from Vector3 import Vector3

class MathPhysics:

    @staticmethod
    def apply_gravity(obj, workspace):
        """
        Pulls the object down based on workspace gravity and object mass.
        Heavier objects accelerate the same (like real gravity) but carry
        more momentum, so they're harder to stop.
        Formula: F = mass * gravity, a = F / mass (simplifies to just gravity)
        """
        gravity_force = workspace.Gravity * obj.Mass
        obj.Acceleration = obj.Acceleration + Vector3(0, -gravity_force / obj.Mass, 0)

    @staticmethod
    def apply_air_resistance(obj, air):
        """
        Slows the object down based on air density and how fast it's moving.
        Faster objects feel more drag. Denser air = more drag.
        Formula: drag = 0.5 * density * velocity^2 * drag_coefficient
        """
        drag_coefficient = 0.47  # roughly a sphere, good default
        speed_squared = obj.Velocity.magnitude_squared()

        if speed_squared == 0:
            return  # not moving, no drag

        drag_magnitude = 0.5 * air.Density * speed_squared * drag_coefficient
        drag_direction = -obj.Velocity.normalize()  # opposite to movement
        drag_force = drag_direction * drag_magnitude

        # a = F / m
        obj.Acceleration = obj.Acceleration + drag_force / obj.Mass

    @staticmethod
    def apply_wind(obj, air):
        """
        Pushes the object in the wind direction based on wind force.
        Heavier objects are pushed less (F = ma, so a = F/m)
        """
        wind_force = air.AirWindDirection.normalize() * air.AirWindForce
        obj.Acceleration = obj.Acceleration + wind_force / obj.Mass

    @staticmethod
    def apply_friction(obj, friction_override=None):
        """
        Slows down horizontal (X and Z) velocity when object is on a surface.
        Uses the object's own friction value unless overridden (e.g. by surface).
        """
        friction = friction_override if friction_override is not None else obj.Friction

        # Only slow down horizontal movement, not vertical (that's gravity's job)
        obj.Velocity = Vector3(
            obj.Velocity.x * (1.0 - friction),
            obj.Velocity.y,
            obj.Velocity.z * (1.0 - friction)
        )

    @staticmethod
    def update_position(obj, delta_time):
        """
        Moves the object based on its velocity.
        Also updates velocity based on acceleration.
        delta_time = time since last frame (keeps physics framerate-independent)
        """
        # Update velocity from acceleration
        obj.Velocity = obj.Velocity + obj.Acceleration * delta_time

        # Update position from velocity
        obj.Position = obj.Position + obj.Velocity * delta_time

        # Reset acceleration (forces are recalculated every frame)
        obj.Acceleration = Vector3(0, 0, 0)

    @staticmethod
    def resolve_bounce(obj, surface_normal):
        """
        Calculates the new velocity after bouncing off a surface.
        surface_normal = the direction the surface is facing (e.g. Vector3(0,1,0) for floor)
        restitution = bounciness (0 = dead stop, 1 = bounces forever, 0.7 = realistic)
        """
        # Only bounce if object is moving INTO the surface
        if obj.Velocity.dot(surface_normal) >= 0:
            return  # already moving away, no bounce needed

        # Reflect velocity off the surface, then reduce by restitution
        reflected = obj.Velocity.reflect(surface_normal)
        obj.Velocity = reflected * obj.Restitution

