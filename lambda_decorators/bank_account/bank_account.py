class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,*amount):
        self.balance += sum(amount)

    def info(self, **details):
        # Merge basic info with extra details
        base = {"owner": self.owner, "balance": self.balance}
        base.update(details)
        return base


acc = BankAccount("Alice", 100)
print(acc.deposit(50, 25, 75))
print(acc.info(branch="NYC"))