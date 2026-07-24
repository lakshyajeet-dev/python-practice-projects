# Create a class:

# BankAccount

# Requirements:

# Private attribute:

# __balance

# Methods:

# deposit(amount)
# withdraw(amount)
# get_balance()

# Rules:

# Deposit amount must be greater than 0.
# Withdrawal should fail if the balance is insufficient.
# Never allow the balance to become negative.


class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # __balance is a private attribute (double underscore makes it private)
    def deposit(self, amount):
        # Deposit must be greater than 0
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be greater than 0 ")  

    def withdraw(self, amount):
        # Withdrawal should fail if balance is insufficient
        if amount <= 0:
            print("Withdrawal amount must be greater than 0 ")
        elif amount > self.__balance:
            print("Insufficient balance ")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")          

    def get_balance(self):
        # Return the current balance
        print(f"Current balance: {self.__balance}")
        return self.__balance

# Example usage
account = BankAccount(100)   # Start with 100 balance
account.get_balance()        # Show balance
account.deposit(50)          # Add 50
account.withdraw(30)         # Withdraw 30
account.withdraw(200)        # Try withdrawing more than balance
account.deposit(-10)         # Try invalid deposit            