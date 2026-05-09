import os

class InsufficientStockError(Exception):
    """Custom exception for stock issues."""
    pass


def load_from_file(filename):
    inventory = []
    if not os.path.exists(filename):
        return inventory

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            try:
                name, price, quantity = line.strip().split(",")
                price = float(price)
                quantity = int(quantity)
                inventory.append({
                    "name": name,
                    "price_tjs": price,
                    "quantity": quantity
                })
            except Exception:
                continue
    return inventory


def save_to_file(inventory, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in inventory:
            f.write(f"{item['name']},{item['price_tjs']},{item['quantity']}\n")  # match test key


def add_product(inventory, name, price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative")

    for item in inventory:
        if item["name"] == name:
            item["quantity"] += quantity
            return inventory

    inventory.append({
        "name": name,
        "price_tjs": price,
        "quantity": quantity
    })
    return inventory


def sell_product(inventory, name, quantity):
    for item in inventory:
        if item["name"] == name:
            if item["quantity"] < quantity:
                raise InsufficientStockError(
                    f"Not enough stock for {name}. Available: {item['quantity']}"
                )
            item["quantity"] -= quantity
            return inventory

    raise ValueError(f"Product {name} not found in inventory")