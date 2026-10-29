# Week 1.5, Session 2: Task 1

# Add type hints to the Point class

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x: float, y: float):
        """
        Creates a Point, given x & y coordinates.
        """

        
        self.y = y
        self.x = x

    def distance(self) -> float:
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, p) -> float:
        """
        Returns distance of this Point from the specified Point.
        """
        if not isinstance(p, (int)):
            raise TypeError("y must be a number")
        
        return math.hypot(self.x - p.x, self.y - p.y)




# Test program

p = Point("two", "one")
print(p.distance())
