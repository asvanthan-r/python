from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self, own, balance):
        self.own =own
        self.balance =balance
    def deposit(self, amount):
        self.balance = self.balance +amount
    def withdraw(self, withdraw):
        self.balance = self.balance - self.withdraw 
        return self.balance
    def display_balance(self):
        print("balance", self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, own, balance, intersetrate):
        super().__init__(own, balance)
        self.interestrate = intersetrate
    def deposit(self, amount):
        super().deposit(amount)
        self.balance = self.balance + ((self.balance *self.interestrate) /100)
        return self.balance
    def withdraw(self, withdraw):
        super().withdraw(withdraw)
        self.balance = self.balance - self.withdraw 
        return self.balance
    def display_balance(balance):
        super().display_balance()
        print("balance", balance)

cust1 = SavingsAccount("Alice", 1000.0, 5.0)
cust1.deposit(555)
#cust1.withdraw(44)
cust1.display_balance()