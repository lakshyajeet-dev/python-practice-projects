# Square a number
def square_normal(x):
    return x * x

square_lambda = lambda x: x * x

print("--- 1. Square a number ---")
print(f"Normal: {square_normal(5)}")
print(f"Lambda: {square_lambda(5)}\n")

# Cube a number
def cube_normal(x):
    return x * x * x

cube_lambda = lambda x: x * x * x
print(f"Normal: {cube_normal(3)}")
print(f"Lambda: {cube_lambda(3)}\n")

# Check if a number is positive
def  is_positive_normal(x):
    return x > 0

is_positive_lambda = lambda x: x > 0
print(f"Normal (10): {is_positive_normal(10)}")
print(f"Lambda (-5): {is_positive_lambda(-5)}\n")


# Find the larger of two numbers
def find_max_normal(a,b):
    if a > b:
        return a
    else:
        return b
find_max_lambda = lambda a,b: a if a > b else b
print(f"Normal (15, 42): {find_max_normal(15, 42)}")
print(f"Lambda (15, 42): {find_max_lambda(15, 42)}\n")    

# Convert Celsius to Fahrenheit
def c_to_f_normal(c):
    return (c * 9/5) + 32

c_to_f_lambda = lambda c: (c * 9/5) + 32
print(f"Normal (25°C): {c_to_f_normal(25)}")
print(f"Lambda (25°C): {c_to_f_lambda(25)}")