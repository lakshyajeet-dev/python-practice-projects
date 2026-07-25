# Mini Project

# Create the following classes.

# Parent Class
# class Person:

# Attributes:

# name
# age

# Method:

# introduce()


# Define a class called Person
class Person:
    def __init__(self, name, age):
        # Constructor: runs when you create a new Person object
        # self.name stores the person's name
        # self.age stores the person's age
        self.name = name
        self.age = age

    def introduce(self):
        # Method to introduce the person
        # Prints the name and age stored in the object
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")
        

# Example usage
person1 = Person("Lakshyajeet", 21)   # Create a Person object
person1.introduce()                   # Call the introduce method
