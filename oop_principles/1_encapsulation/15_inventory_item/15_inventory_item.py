class InventoryItem:


    def __init__(self, name, price, initial_stock=0):
        if price <= 0:
            raise ValueError("Price must be positive")
        if initial_stock < 0:
            raise ValueError("Initial stock cannot be negative")

        self._name       = name
        self._price      = price
        self._stock      = initial_stock
        self._total_sold = 0


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
        self._stock      -= quantity
        self._total_sold += quantity


    def get_is_in_stock(self):
        return self._stock > 0

    def is_low_stock(self, threshold=5):
        return self._stock <= threshold


    def get_total_value(self):
        return round(self._stock * self._price, 2)


    def discount(self, percentage):
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
        self._price = round(self._price * (1 - percentage / 100), 2)


    def sell_all(self):
        revenue    = self.get_total_value()
        self._total_sold += self._stock
        self._stock = 0
        return revenue


    def get_total_sold(self):
        return self._total_sold


    def __str__(self):
        return f"{self._name}: ${self._price}, Stock: {self._stock} units, Value: ${self.get_total_value()}"



item = InventoryItem("Laptop", 999.99, 10)
print(item)

print(item.get_is_in_stock())
print(item.is_low_stock())
print(item.is_low_stock(15))

item.restock(5)
print(item.get_stock())
print(item.get_total_value())

item.sell(3)
print(item.get_stock())

try:
    item.sell(20)
except ValueError as e:
    print(e)

try:
    item.set_price(-50)
except ValueError as e:
    print(e)

try:
    item.restock(-5)
except ValueError as e:
    print(e)


phone = InventoryItem("Phone", 599.99, 3)
print(phone.is_low_stock())


tablet = InventoryItem("Tablet", 299.99, 0)
print(tablet.get_is_in_stock())


item.discount(10)
print(item.get_price())

revenue = item.sell_all()
print(revenue)
print(item.get_total_sold())
