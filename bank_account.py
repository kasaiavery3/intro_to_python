# Exercise: Create Your Own Class
# BankAccount class
class BankAccount():
    def __init__(self, kind, owner):
        self.kind = kind
        self.owner = "Kasai"
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.amount -= amount
        if (self.amount < 0):
            self.overdraft_fees += 20
        return amount