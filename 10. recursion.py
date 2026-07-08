# Project 1 — Recursive Countdown
def countdown(n):                  # Define a function named countdown with parameter n
    if n == 0:                     # Base case: when n reaches 0
        print("Blast off!")        # Print final message
    else:                          
        print(n)                   # Print current number
        countdown(n - 1)           # Call the same function again with n-1
countdown(5) 

# Project 2 — Recursive Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) 
print("Factorial of 5:", factorial(5))

# Project 3 — Sum 1 to N
def sum_to_n(n):
    if n == 0:                     # Base case: sum of 0 is 0
        return 0
    else:
        return n + sum_to_n(n - 1) # Recursive step: add n + sum of (n-1)

print("Sum 1 to 5:", sum_to_n(5))


# Project 4 — Reverse String 
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
          return reverse_string(s[1:]) + s[0] 
print("Reverse:", reverse_string("hello"))    