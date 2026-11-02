# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

import shapes

Circle = shapes.Circle(2.5)

print(Circle)
print(Circle.area())
print(Circle.perimeter())
Circle.set_colour('green')
print(Circle)
Circle.set_position(1.6, 3.2)
print(Circle)