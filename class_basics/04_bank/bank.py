class BankAccount:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f"Balance: ${self.balance}")
        else:
            print(f"Insufficient funds! Balance: ${self.balance}")

account = BankAccount("Alice")
account.deposit(100)
account.withdraw(30)
account.withdraw(80)