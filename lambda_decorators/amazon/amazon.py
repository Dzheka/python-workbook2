products = [
    {"name": "Laptop",  "price": 1200, "rating": 4.5},
    {"name": "Phone",   "price": 800,  "rating": 4.8},
    {"name": "Headset", "price": 150,  "rating": 3.9},
    {"name": "Tablet",  "price": 600,  "rating": 4.2},
    {"name": "Cable",   "price": 10,   "rating": 3.5},
]

def affordable(products, max_price):
    for product in products:
        if product["price"] <= max_price:
            yield product

best_rated = lambda items: max(items, key=lambda p: p["rating"])

def total_price(products):
    if not products:
        return 0
    return products[0]["price"] + total_price(products[1:])

print(list(affordable(products, 700)))   # → [Phone excluded, Headset, Tablet, Cable]
print(best_rated(products))              # → {"name": "Phone", ...}
print(total_price(products))             # → 2760
print(total_price([]))                   # → 0