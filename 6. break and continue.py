# Project 1 — Password Retry
# Keep asking until correct.
# Use break.
# Password Retry
correct_password = "python123"

while True:                                # Infinite loop
    password = input("Enter password: ")
    if password == correct_password:        # If correct
        print("Access granted ✅")
        break                               # Exit loop immediately
    else:
        print("Wrong password ❌, try again")


# Project 2 — Number Filter
# Print numbers except multiples of 3.
# Use continue.
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)

#  Project 3 — Search Character
# Input word.
# Stop when target found.
word = input("Enter a word: ") 
target = input("Enter a character to search for: ")
for char in word:
    if char == target:
        print(f"Character '{target}' found in word '{word}'.")
        break
    else:
        print("Character not found.")

#  Project 4 — Menu Program
# Repeat until user chooses Exit.
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Exit")
    choice = input("Enter a choice (1 or 2):")
    if choice == "1":
        print("Heelo!")
    elif choice == "2":
        print("Exiting program.")
        break                              
    else:
        print("Invalid choice.")
       
