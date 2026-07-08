# Project 1 — Duplicate Remover
# Input list → remove duplicates.
numbers = [1, 2, 2, 3, 4, 4, 5] 
unique = set(numbers)
print("Unique numbers:", unique)

# Project 2 — Common Students
# Compare two classes.
classA = {"Lakshya", "Ravi", "Neha"}   # Students in Class A
classB = {"Ravi", "Neha", "Amit"}      # Students in Class B
common = classA & classB
print("Common students:", common)

# Project 3 — Username Availability Checker
# Store existing usernames.
# Username Availability Checker with retry

existing_users = {"admin", "lakshya", "guest"}   # Already taken usernames

while True:                                      # Infinite loop until break
    new_user = input("Enter new username: ")
    if new_user in existing_users:               # Check if username exists
        print("Username not available ❌, try again")
    else:
        print("Username available ✅")
        break                                   # Exit loop when username is valid


# Project 4 — Unique Word Counter
# Count unique words.
sentence = input("Enter a sentence: ")
words = sentence.split()              # Split sentence into words
unique_words = set(words)             # Convert list to set (unique words)
print("Unique words:", unique_words)
print("Count:", len(unique_words))    # Count how many unique words
