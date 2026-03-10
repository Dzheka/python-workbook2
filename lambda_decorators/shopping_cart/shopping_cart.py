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
            price = item["price"]
            name = item["name"]
            if name in discounts:
                price = price * (1 - discounts[name] / 100)
            total += price
        return total

    def summary(self):
        return {
            "owner": self.owner,
            "items": [item["name"] for item in self.items],
            "total": self.total()
        }
