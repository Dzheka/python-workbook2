class InventoryItem:
    def __init__(self, name, price, initial_stock=0):
        if price <= 0:
            raise ValueError("Price must be positive")
        self._name = name
        self._price = price
        self._stock = initial_stock

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price <= 0:
            raise ValueError("Price must be positive")
        self._price = price

    def get_stock(self):
        return self._stock

    def restock(self, quantity):
        if quantity <= 0:
            raise ValueError("Restock quantity must be positive")
        self._stock += quantity

    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("Sell quantity must be positive")
        if quantity > self._stock:
            raise ValueError(f"Cannot sell {quantity} units. Only {self._stock} units in stock.")
        self._stock -= quantity

    def get_is_in_stock(self):
        return self._stock > 0

    def is_low_stock(self, threshold=5):
        return self._stock <= threshold

    def get_total_value(self):
        return self._stock * self._price

    def __str__(self):
        return f"{self._name}: ${self._price:.2f}, Stock: {self._stock} units, Value: ${self.get_total_value():.2f}"
