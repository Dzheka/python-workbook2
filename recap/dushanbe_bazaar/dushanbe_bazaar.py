import os

class InsufficientStockError(Exception):
    """Custom exception for stock issues."""
    pass


def load_from_file(filename):
    "your code"


def save_to_file(inventory, filename):
    "your code"


def add_product(inventory, name, price, quantity):
    "your code"


def sell_product(inventory, name, quantity):
    for item in inventory:
        if item['name'] == name:
            if item['quantity'] < quantity:
                raise InsufficientStockError(f"Not enough {name} in stock!")
            item['quantity'] -= quantity
            return True

    raise ValueError(f"Product {name} not found!")