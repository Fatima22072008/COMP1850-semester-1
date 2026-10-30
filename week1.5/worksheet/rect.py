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
        if not isinstance(width, (int)):
            raise TypeError("must be an interger")
        elif width <= 0:
            raise ValueError("must be more than 0")

        if not isinstance(height, (int)):
            raise TypeError("must be an interger")
        elif height <= 0:
            raise ValueError("must be more than 0")
        
        self.width = width
        self.height = height


        # Implement methods is_square(), area() & perimeter() here
        # (See README.md for details of what they should do)
        
    def is_square(self):
        """
        checks if its a square
         """
        if self.width == self.height:
            return True 
        else:
            return False

    def area(self):
        """
        calculated the rectangle length
        """
        Rectangle = self.width * self.height
        return Rectangle

    def perimeter(self):
        """
        calculates the rectangle perimeter
        """
        rectangle_perimeter = (self.width * 2) + (self.height * 2)
        return rectangle_perimeter
