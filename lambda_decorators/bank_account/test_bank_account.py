from bank_account import BankAccount

def test_initial_balance():
    acc = BankAccount("Alice")
    assert acc.balance == 0

def test_deposit_single():
    acc = BankAccount("Bob", 100)
    acc.deposit(50)
    assert acc.balance == 150

def test_deposit_multiple():
    acc = BankAccount("Bob", 0)
    acc.deposit(10, 20, 30)
    assert acc.balance == 60

def test_info_basic():
    acc = BankAccount("Alice", 200)
    assert acc.info() == {"owner": "Alice", "balance": 200}

def test_info_with_extra():
    acc = BankAccount("Alice", 200)
    result = acc.info(branch="NYC", tier="gold")
    assert result["branch"] == "NYC"
    assert result["tier"] == "gold"
    assert result["owner"] == "Alice"