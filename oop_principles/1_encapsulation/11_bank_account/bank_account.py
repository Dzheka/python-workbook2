class BankAccount:
    def __init__(self, account_holder, initial_balance):
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
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds. Balance: ${self._balance:.2f}, Attempted transfer: ${amount:.2f}")
        self.withdraw(amount)
        target_account.deposit(amount)

    def __str__(self):
        return f"Account holder: {self._account_holder}, Balance: ${self._balance:.2f}"

# Create accounts
alice_account = BankAccount("Alice", 1000.0)
bob_account = BankAccount("Bob", 500.0)

print(alice_account)  # "Account holder: Alice, Balance: $1000.00"
print(alice_account.get_balance())  # 1000.0

# Deposit money
alice_account.deposit(250.0)
print(alice_account.get_balance())  # 1250.0

# Withdraw money
alice_account.withdraw(100.0)
print(alice_account.get_balance())  # 1150.0

# Transfer money
alice_account.transfer(200.0, bob_account)
print(alice_account.get_balance())  # 950.0
print(bob_account.get_balance())    # 700.0

# Invalid operations (should raise ValueError)
try:
    alice_account.withdraw(2000.0)  # Insufficient funds
except ValueError as e:
    print(e)  # "Insufficient funds. Balance: $950.00, Attempted withdrawal: $2000.00"

try:
    alice_account.deposit(-50.0)  # Negative deposit
except ValueError as e:
    print(e)  # "Deposit amount must be positive"

try:
    bob_account.withdraw(0)  # Zero withdrawal
except ValueError as e:
    print(e)  # "Withdrawal amount must be positive"

# Invalid account creation
try:
    invalid_account = BankAccount("Charlie", -100.0)
except ValueError as e:
    print(e)  # "Initial balance cannot be negative"