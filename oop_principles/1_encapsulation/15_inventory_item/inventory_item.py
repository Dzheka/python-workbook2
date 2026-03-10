class InventoryItem:
    def __init__(self,name, price, initial_stock = 0):
        self.__name = name
        self.price = price
        self._stock = initial_stock

    def get_name(self):
        return f"{self.__name}"

    def get_price(self):
        return f"{self.price}"

    def set_price(self,price):
        if price < 0:
            raise ValueError("Price must be positive")
        self.price = price

    def get_stock(self):
        return self._stock

    def restock(self,quantity):
        if quantity <= 0:
            raise ValueError("Restock quantity must be positive")
        self._stock += quantity

    def sell(self,quantity):
        if self._stock < quantity:
            raise  ValueError(f"Cannot sell {quantity} units. Only {self._stock} units in stock")
        self._stock -= quantity

    def get_is_in_stock(self):
        if self._stock > 0:
            return True
        return False

    def is_low_stock(self,threshold=5):
        if self._stock <= threshold:
            return True
        return False

    def get_total_value(self):
        return self._stock * self.price

    def __str__(self):
        return f"{self.__name}: ${self.price}, Stock: {self._stock}, Value: {self.get_total_value()}"




# Create inventory item
item = InventoryItem("Laptop", 999.99, 10)
print(item)  # "Laptop: $999.99, Stock: 10 units, Value: $9999.90"

# Check stock status
print(item.get_is_in_stock())      # True
print(item.is_low_stock())         # False (stock > 5)
print(item.is_low_stock(15))       # True (stock <= 15)

# Restock operations
item.restock(5)
print(item.get_stock())            # 15
print(item.get_total_value())      # 14999.85

# Sales operations
item.sell(3)
print(item.get_stock())            # 12

# Try to sell more than available
try:
    item.sell(20)                  # Should fail - not enough stock
except ValueError as e:
    print(e)  # "Cannot sell 20 units. Only 12 units in stock."

# Price validation
try:
    item.set_price(-50)            # Should fail - negative price
except ValueError as e:
    print(e)  # "Price must be positive"

# Invalid operations
try:
    item.restock(-5)               # Should fail - negative restock
except ValueError as e:
    print(e)  # "Restock quantity must be positive"

# Low stock scenario
phone = InventoryItem("Phone", 599.99, 3)
print(phone.is_low_stock())  # True (stock <= 5)

# Out of stock scenario
tablet = InventoryItem("Tablet", 299.99, 0)
print(tablet.get_is_in_stock())    # False