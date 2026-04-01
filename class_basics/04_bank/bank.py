class BankAccount:
    def init(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Balance: ${self.balance}")
        else:
            print(f"Insufficient funds! Balance: ${self.balance}")
