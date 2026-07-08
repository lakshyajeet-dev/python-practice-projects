# Mini Project 1 — Notes App
# Menu:
# 1 Add
# 2 View
# 3 Exit
# Store notes.
def add_note():                             # Define a function to add a note
    note = input("Enter your note: ")       # Ask user for note text
    with open("notes.txt", "a") as f:       # Open file in append mode ("a")
        f.write(note + "\n")                # Write note + newline into file
    print("Note added ✅")                   # Confirm to user

def view_notes():                           # Define a function to view notes
    try:
        with open("notes.txt", "r") as f:   # Open file in read mode ("r")
            print("\nYour Notes:")          
            print(f.read())                 # Read entire file and print
    except FileNotFoundError:               # If file doesn't exist
        print("No notes found ❌")

while True:                                 # Infinite loop for menu
    print("\nMenu:\n1 Add\n2 View\n3 Exit") # Show menu options
    choice = input("Enter choice: ")        # Ask user for choice
    if choice == "1":                       # If user chooses Add
        add_note()
    elif choice == "2":                     # If user chooses View
        view_notes()
    elif choice == "3":                     # If user chooses Exit
        print("Exiting Notes App 👋")
        break                               # Exit loop
    else:
        print("Invalid choice ❌")          # Handle wrong input
  


# Mini Project 2 — Student Record Saver
# Save:
# name
# marks
# Student Record Saver
name = input("Enter student name: ")        # Ask user for name
marks = input("Enter marks: ")              # Ask user for marks

with open("student_record.txt", "w") as f:  # Open file in write mode ("w")
    f.write(f"Name: {name}\nMarks: {marks}\n") # Save name and marks

print("Record saved")                    # Confirm to user


# Mini Project 3 — Journal
# Append entries.
# Journal App
entry = input("Write your journal entry: ") # Ask user for journal text

with open("journal.txt", "a") as f:         # Open file in append mode ("a")
    f.write(entry + "\n")                   # Add entry with newline

print("Entry added to journal")          # Confirm to user




