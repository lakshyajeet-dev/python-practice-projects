# Project 1 — Student Record System
# Store:
# •	name 
# •	age 
# •	marks 
student = {
    "name": "Lakshyajeet",
    "age": 20,
    "marks": 85
}
print("Name:", student["name"])    # Access value by key
print("Age:", student["age"])
print("Marks:", student["marks"])

# Project 2 — Contact Book
# Search by name.
contacts = {
    "Ravi": "9876543210",
    "Neha": "9123456789",
    "Amit": "9988776655"
}
name = input("Enter name to search:")
if name in contacts:
    print("Contact number:", contacts[name])
else:
    print("Contact not found.")

# Project 3 — Expense Tracker
# Category → amount.
expenses = {
    "Food": 1200,
    "Transport": 500,
    "Shopping": 2000
}
total = sum(expenses.values())
print("Expenses:", expenses)
print("Total spent:", total)


# Project 4 — Login System
# Username → password.
users = {
    "admin": "1234",
    "lakshya": "python123",
    "guest": "guest"
}
username = input("Enter username: ")
password = input("Enter password: ")
if username in users and users[username] == password:
    print("Login successful")
else:
    print("Invalid details")
