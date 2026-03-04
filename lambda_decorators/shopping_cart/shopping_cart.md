**Topic:** Amazon | **Concept:** OOP + *args / **kwargs

Write a class `ShoppingCart` with:
- `__init__(self, owner)`
- `add(*items)` — each item is a dict `{"name": ..., "price": ...}`; adds all to the cart
- `total(**discounts)` — calculates total price. `discounts` maps item name → discount percent (0–100)
- `summary()` — returns `{"owner": ..., "items": [...names], "total": ...}`

```python
# Your code here
```

**Expected output:**
```python
cart = ShoppingCart("Alice")
cart.add({"name": "Book", "price": 20}, {"name": "Pen", "price": 5})
cart.total()             # → 25
cart.total(Book=50)      # → 15.0  (Book is 50% off)
cart.summary()           # → {"owner": "Alice", "items": ["Book", "Pen"], "total": 25}
```

---