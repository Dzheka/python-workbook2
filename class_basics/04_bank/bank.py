class BankAccount:
    def __init__(self, owner_name, balance= 0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Balance: ${self.balance}")
        elif amount > self.balance:
            print(f"Insufficient funds! Balance: ${self.balance}")



account = BankAccount("Alice")
account.deposit(100)    # Balance: $100
account.withdraw(30)    # Balance: $70
account.withdraw(80)    # Insufficient funds! Balance: $70