# Task: Create a class hierarchy in Python to demonstrate method overriding.
# Subclasses:
# Rectangle: Overrides area() to return length × width.
# Circle: Overrides area() to return π × r².
# Execution: Create one object of each child class, call .area(), and observe how the same method name produces different outputs.

import math   # We need math module for π (pi)

# Parent class
class Shape:
    def area(self):
        # This is a generic method. It doesn't calculate anything here.
        # Child classes will override this method with their own formulas.
        print("Area method not implemented for generic Shape.")

# Child class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        # Constructor stores length and width
        self.length = length
        self.width = width

    def area(self):
        # Override the parent area() method
        # Formula: length × width
        return self.length * self.width

# Child class Circle
class Circle(Shape):
    def __init__(self, radius):
        # Constructor stores radius
        self.radius = radius

    def area(self):
        # Override the parent area() method
        # Formula: π × r²
        return math.pi * (self.radius ** 2)


# Create objects
rect = Rectangle(10, 5)   # Rectangle with length=10, width=5
circle = Circle(7)        # Circle with radius=7

# Call area() method
print("Rectangle area:", rect.area())
print("Circle area:", circle.area())

        