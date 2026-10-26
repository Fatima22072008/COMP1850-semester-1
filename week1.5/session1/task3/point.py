# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x1_coordinate, y1_coordinate):

        self.x1 = x1_coordinate
        self.y1 = y1_coordinate

    # Add distance() method here
    def distance(self):

        print(math.sqrt( (self.x1 ** 2) + (self.y1 ** 2) ))

    # Add distance_to() method here
    def distance_to(self, secondObject):

        coordinateX = (self.x1 - secondObject.x1) ** 2
        coordinateY = (self.y1 - secondObject.y1) ** 2
        print(math.sqrt(coordinateX + coordinateY))
    # (This will need a parameter representing another point)


object1 = Point(2, 4)
object2 = Point(1, 2)
object1.distance()
object2.distance()
object1.distance_to(object2)

# Finally, add code here to demonstrate use of Point
