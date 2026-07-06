# Project 1 — Eligibility Checker
# Input:
# •	age 
# •	CGPA 
# Decide eligibility.
age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))
if age>= 18 and cgpa >= 5.0:
    print("You are eligible.")
else:
    print("Not eligible.")

# Project 2 — Login System
# Input:
# •	username 
# •	password 
# Compare.
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "password123":
    print("Login successful.")
else:
    print("Invalid username or password.")

# Project 3 — Simple Calculator
# Take operator choice.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    result = num1 + num2
    print("Result:", result)
elif operator == "-":
    result = num1 - num2
    print("Result:", result)
elif operator == "*":
    result = num1 * num2
    print("Result:", result)
elif operator == "/":
    result = num1 / num2
    print("Result:", result)
else:
    print("Invalid operator.")

# Project 4 — Temperature Checker
# Input temperature.
# Print:
# Cold
# Normal
# Hot
temp = float(input("Enter the temprature in celcius: "))
if temp < 0:
    print("Cold")
elif temp >= 0 and temp <= 30:
    print("Normal")
else:
    print("Hot")
