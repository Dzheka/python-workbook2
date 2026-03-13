class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add(self, *items):
        for item in items:
            self.items.append(item)

    def total(self, **discounts):
        final_price = 0.0
        for item in self.items:
            price = item["price"]
            discount_percent = discounts.get(item["name"], 0)
            final_price += price * (1 - discount_percent / 100)
        return final_price

    def summary(self):
        return {
            "owner": self.owner,
            "items": [item["name"] for item in self.items],
            "total": self.total()
        }

cart = ShoppingCart("Alice")
cart.add({"name": "Book", "price": 20}, {"name": "Pen", "price": 5})

print(cart.total())
print(cart.total(Book=50))
print(cart.summary())