# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
import geometry

point = geometry.Point(1.0, 1.5)
circle = geometry.Circle(2.7)
if point in circle:
    print("point is in cirlce")