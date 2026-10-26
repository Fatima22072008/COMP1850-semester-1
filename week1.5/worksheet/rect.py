# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width

        if self.width <= 0:
            raise ValueError
        elif type(self.width) != int:
            raise TypeError
        
        self.height = height

        if self.height <= 0:
            raise ValueError
        elif type(self.height) != int:
            raise TypeError

        # Implement methods is_square(), area() & perimeter() here
        # (See README.md for details of what they should do)
        
    def is_square(self):

        if self.width == self.height:
            return True 
        else:
            return False

    def area(self):

        Rectangle = self.width * self.height
        return Rectangle

    def perimeter(self):

        rectangle_perimeter = (self.width * 2) + (self.height * 2)
        return rectangle_perimeter
