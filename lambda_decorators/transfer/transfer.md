#  **Topic:** Bank | **Concept:** Decorator

Write a decorator `log_transaction` that:
- prints `"Transaction started"` before the function runs
- prints `"Transaction finished: <return_value>"` after it runs
- returns the original return value unchanged

Apply it to a function `transfer(amount)` that simply returns the amount.

```python
# Your code here

@log_transaction
def transfer(amount):
    return amount
```

**Expected output:**
```
transfer(500)
# Transaction started
# Transaction finished: 500
# → 500
```

---