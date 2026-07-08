# Create a simple calculator.
# Requirements:
# 1.	Ask the user for two numbers. 
# 2.	Ask the user to choose: 
# o	+ 
# o	- 
# o	* 
# o	/ 
# 3.	Use exception handling to: 
# o	Handle invalid number input (ValueError) 
# o	Handle division by zero (ZeroDivisionError) 
# 4.	Print a meaningful error message instead of crashing.

try:
    # Step 1: Ask for two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Step 2: Ask for operation
    op = input("Choose operation (+, -, *, /): ")

    # Step 3: Perform calculation
    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        try:
            print("Result:", num1 / num2)   # Division
        except ZeroDivisionError:           # Handle divide by zero
            print("Error: Cannot divide by zero")
    else:
        print("Invalid operation")

except ValueError:                          # Handle invalid number input
    print("Error: Please enter valid numbers")
