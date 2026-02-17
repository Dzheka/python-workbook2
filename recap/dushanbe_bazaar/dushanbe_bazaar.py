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
    "your code"
