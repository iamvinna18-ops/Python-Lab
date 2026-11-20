# Lab Exercise 1:Bank Account System Using OOP

# Bank Account System using OOP

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance!")

    def display(self):
        print("\nAccount Holder:", self.name)
        print("Current Balance:", self.balance)


# Creating Object

account = BankAccount("Ajitesh", 10000)

account.display()

account.deposit(5000)
account.withdraw(2000)

account.display()