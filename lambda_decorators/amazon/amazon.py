products = [
    {"name": "Laptop",  "price": 1200, "rating": 4.5},
    {"name": "Phone",   "price": 800,  "rating": 4.8},
    {"name": "Headset", "price": 150,  "rating": 3.9},
    {"name": "Tablet",  "price": 600,  "rating": 4.2},
    {"name": "Cable",   "price": 10,   "rating": 3.5},
]

def affordable(productss,max_price):
    for product in productss:
        if product["price"] <= max_price:
            yield product


best_rated = lambda prods: max(prods, key=lambda x: x["rating"]) if prods else None

def total_price(productss):
    if not productss:
        return 0
    return productss[0]["price"] + total_price(productss[1:])


print(list(affordable(products, 700)))
best_rated(products)              # → {"name": "Phone", ...}
total_price(products)# → 2760
total_price([])                   # → 0