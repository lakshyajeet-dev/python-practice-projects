# Project 1 — Multiplication Table
# Input number.
# Print table.
num = int(input("Enter a number: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")

# Project 2 — Countdown
# Input:
# 10
# Output:
# 10 9 8 7 ...
n = int(input("Enter a number to start countdown: "))
for i in range(n, 0, -1):
    print(i, end=" ")

# Project 3 — Character Counter
# Input word.
# Print each character.
word = input("Enter a word: ")
for char in word:
    print(char)

# Project 4 — Sum of N Numbers
# Input:
# 5
# Output:
# 15
n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total += i
    print(f"Sum of first {n} numbers is: {total}")

# Project 5 — Password Attempts
# Loop until correct password.
correct_password = "python123"        # Store the correct password

while True:                           # Infinite loop until break
    password = input("Enter password: ") # Ask user for password
    if password == correct_password:     # Check if input matches
        print("Access granted ✅")        # Success message
        break                            # Exit loop
    else:
        print("Wrong password, try again ❌") # Retry message

