from abc import ABC, abstractmethod   # Import tools for abstract classes
import math                           # Import math for π (pi)

# Parent abstract class
class Shape(ABC):                     # Shape inherits from ABC (Abstract Base Class)
    @abstractmethod                   # Decorator: forces child classes to implement this method
    def area(self):
        pass                          # No implementation here, just a placeholder


# Child class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):                   # Must implement area() because parent made it abstract
        return self.length * self.width


# Child class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                   # Must implement area() because parent made it abstract
        return math.pi * (self.radius ** 2)


# Create objects
rect = Rectangle(10, 5)               # Rectangle with length=10, width=5
circle = Circle(7)                    # Circle with radius=7

# Call area() method
print("Rectangle area:", rect.area())
print("Circle area:", circle.area())
