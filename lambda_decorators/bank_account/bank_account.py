class BankAccount:


    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance


    def deposit(self, *amounts):
        for amount in amounts:
            self.balance += amount


    def info(self, **details):
        result = {
            "owner":   self.owner,
            "balance": self.balance
        }


        for key, value in details.items():
            result[key] = value

        return result


acc = BankAccount("Alice", 100)
acc.deposit(50, 25, 75)

print(acc.balance)
print(acc.info(branch="NYC"))
