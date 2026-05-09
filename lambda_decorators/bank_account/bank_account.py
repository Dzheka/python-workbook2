class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, *amounts):
        for amount in amounts:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            self.balance += amount

    def info(self, **details):
        owner = {"owner": self.owner, "balance": self.balance}
        owner.update(details)
        return owner
    
acc = BankAccount("Alice", 100)
print(acc.deposit(50, 25, 75))
print(acc.balance )         # → 250
print(acc.info(branch="NYC")) # → {"owner": "Alice", "balance": 250, "branch": "NYC"}