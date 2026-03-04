**Topic:** Amazon | **Concept:** Generator + Lambda + Recursion

You have a list of products:
```python
products = [
    {"name": "Laptop",  "price": 1200, "rating": 4.5},
    {"name": "Phone",   "price": 800,  "rating": 4.8},
    {"name": "Headset", "price": 150,  "rating": 3.9},
    {"name": "Tablet",  "price": 600,  "rating": 4.2},
    {"name": "Cable",   "price": 10,   "rating": 3.5},
]
```

Write:
1. A **generator** `affordable(products, max_price)` — yields products whose price <= max_price
2. A **lambda** `best_rated` — takes a list of products, returns the one with the highest rating
3. A **recursive** function `total_price(products)` — sums all prices (no loops, no `sum()`)

```python
# Your code here
```

**Expected output:**
```python
list(affordable(products, 700))   # → [Phone excluded, Headset, Tablet, Cable]
best_rated(products)              # → {"name": "Phone", ...}
total_price(products)             # → 2760
total_price([])                   # → 0
```