# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
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


class circle: 
    """
    calculates the radius then uses it calculate the are and perimeter
    """
    def __init__(self, radius, centre ):

        self.centre = centre 
        self.radius = radius

    def area(self):

        circle_area = math.pi * (self.radius ** 2)
        return circle_area

    def perimeter(self):

        circle_perimeter = math.pi * (self.radius * 2)
        return circle_perimeter
# Finally, add code here to demonstrate use of Point