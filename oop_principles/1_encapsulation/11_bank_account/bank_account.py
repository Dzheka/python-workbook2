class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._account_holder = account_holder
        self._balance = initial_balance

    def get_account_holder(self):
        return self._account_holder

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds. Balance: ${self._balance:.2f}, Attempted withdrawal: ${amount:.2f}")
        self._balance -= amount

    def transfer(self, amount, target_account):
        self.withdraw(amount)
        target_account.deposit(amount)

    def __str__(self):
        return f"Account holder: {self._account_holder}, Balance: ${self._balance:.2f}"
