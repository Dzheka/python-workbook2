#  **Topic:** Bank | **Concept:** OOP + *args / **kwargs

Write a class `BankAccount` with:
- `__init__(self, owner, balance=0)`
- `deposit(*amounts)` — adds all given amounts to balance
- `info(**details)` — returns a dict with `"owner"` and `"balance"`, plus any extra key-value pairs passed in

```python
# Your code here
```

**Expected output:**
```python
acc = BankAccount("Alice", 100)
acc.deposit(50, 25, 75)
acc.balance          # → 250
acc.info(branch="NYC")  # → {"owner": "Alice", "balance": 250, "branch": "NYC"}
```

---