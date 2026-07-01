# Project 1 — Introduction Program
# Ask:
# Name
# Age
# City
# Print:
# Hello ___
# You are ___ years old
# You live in ___
# ________________________________________
# Project 1: Introduction Program
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print(f"Hello {name}")
print(f"You are {age} years old")
print(f"You live in {city}")

# Project 2 — Age After 5 Years
# Input age.
# Output:
# After 5 years you will be X
age = int(input("Enter your age: "))
future_age = age + 5
print("After 5 years you will be", future_age)


# Project 3 — Student Details
# Input:
# •	name 
# •	semester 
# •	branch 
# Print formatted output.

# Project 3: Student Details
name = input("Enter student name: ")
semester = input("Enter semester: ")
branch = input("Enter branch: ")

print("\n--- Student Details ---")
print(f"Name     : {name}")
print(f"Semester : {semester}")
print(f"Branch   : {branch}")


# Project 4 — Simple Calculator
# Input:
# Number 1
# Number 2
# Print:
# Addition
# Subtraction
# Multiplication
# Project 4: Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition       : {num1 + num2}")
print(f"Subtraction    : {num1 - num2}")
print(f"Multiplication : {num1 * num2}")




