# A bad class implementation

# What does the runtime error mean? its not being passed through the function

# How do we fix the code? by using self

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate


p = Point(1.5, 2.0) # passes through the function
print(p.x)
print(p.y)
