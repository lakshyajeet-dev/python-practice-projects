# Project 1 — Calculator Using Functions
# Functions:
# •	add 
# •	subtract 
# •	multiply 
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero not allowed."
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
op = input("Choose an operator (+, -, *. /): ")
if op == "+":
    print("Result:", add(x, y))
elif op == "-":
    print("Result:", subtract(x, y))
elif op == "*":
    print("Result:", multiply(x, y))
elif op == "/":
    print("Result:", divide(x, y))
else:
    print("Invalid operator.")

# Project 2 — Student Grade Checker
# Function:
# •	calculate_grade() 
# Student Grade Checker

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

score = int(input("Enter marks: "))
print("Grade:", calculate_grade(score))

# Project 3 — Username Formatter
# Function:
# •	clean_username() 
def clean_username(username):
    return username.strip().replace(" ", "_").lower()
user = input("Enter username: ")
print("Formatted username:", clean_username(user))

# Project 4 — Password Validator
# Function:
# •	validate() 
def validate(password):
    if len(password) < 6:
        return "Password too short "
    elif not any(char.isdigit() for char in password):
        return "Password must contain a number "
    elif not any(char.isalpha() for char in password):
        return "Password must contain a letter "
    else:
        return "Password is valid "

pwd = input("Enter password: ")
print(validate(pwd))












