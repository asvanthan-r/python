class BankAccount:
    def __init__(self, owner:str, balance:float=0):
        self.owner =owner
        self.balance = balance
    def deposit(self, money_to_be_added):
        self.balance = self.balance + money_to_be_added
    def withdraw(self, withdraw_amount):
        if self.balance<withdraw_amount:
            print("Insufficient funds")
            self.get_balance()
        else:
            self.balance = self.balance - withdraw_amount
    def get_balance(self):
        print(f"Balance: {self.balance}")

cust1 = BankAccount("Alice", 1000.0)
cust1.get_balance()
cust1.deposit(500.0)
cust1.get_balance()
cust1.withdraw(6500.0)
