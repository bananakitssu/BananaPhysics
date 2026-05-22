import math

class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        """Multiply by a scalar (e.g. vector * 2.0)"""
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        """Allow scalar * vector too"""
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide a Vector3 by zero")
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __neg__(self):
        """Flip direction: -vector"""
        return Vector3(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return f"Vector3({self.x:.4f}, {self.y:.4f}, {self.z:.4f})"

    # --- Math ---

    def magnitude(self):
        """Length of the vector"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def magnitude_squared(self):
        """Length squared — faster than magnitude() when you don't need the sqrt"""
        return self.x**2 + self.y**2 + self.z**2

    def normalize(self):
        """Returns a unit vector (length = 1) pointing the same direction"""
        mag = self.magnitude()
        if mag == 0:
            return Vector3(0, 0, 0)
        return self / mag

    def dot(self, other):
        """
        Dot product — used for:
        - Checking if two vectors point the same way (positive = same, negative = opposite)
        - Calculating angles between vectors
        - Projecting one vector onto another
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        """
        Cross product — returns a vector perpendicular to both.
        Used for:
        - Calculating torque (rotational force)
        - Finding surface normals
        """
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def distance_to(self, other):
        """Distance between two points"""
        return (self - other).magnitude()

    def angle_to(self, other):
        """Angle in radians between two vectors"""
        dot = self.dot(other)
        mags = self.magnitude() * other.magnitude()
        if mags == 0:
            return 0.0
        return math.acos(max(-1.0, min(1.0, dot / mags)))

    def reflect(self, normal):
        """
        Reflect this vector off a surface with the given normal.
        Used for bounce direction calculation.
        Formula: v - 2(v·n)n
        """
        return self - normal * (2 * self.dot(normal))

    def lerp(self, other, t):
        """
        Linear interpolation between this vector and another.
        t=0 returns self, t=1 returns other.
        Useful for smooth transitions.
        """
        return self + (other - self) * t

    def copy(self):
        return Vector3(self.x, self.y, self.z)

    @staticmethod
    def zero():
        return Vector3(0, 0, 0)

    @staticmethod
    def up():
        return Vector3(0, 1, 0)

    @staticmethod
    def down():
        return Vector3(0, -1, 0)

    @staticmethod
    def right():
        return Vector3(1, 0, 0)

    @staticmethod
    def forward():
        return Vector3(0, 0, 1)

