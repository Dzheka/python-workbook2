class ShoppingCart:


    def __init__(self, owner):
        self.owner = owner
        self.items = []


    def add(self, *items):
        for item in items:
            self.items.append(item)


    def total(self, **discounts):
        total = 0

        for item in self.items:
            name  = item["name"]
            price = item["price"]


            if name in discounts:
                discount = discounts[name]
                price    = price * (1 - discount / 100)

            total = total + price

        return total


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
