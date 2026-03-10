class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, *amounts):
        for amount in amounts:
            self.balance += amount

    def info(self, **kwargs):
        result = {"owner": self.owner, "balance": self.balance}
        result.update(kwargs)
        return result
