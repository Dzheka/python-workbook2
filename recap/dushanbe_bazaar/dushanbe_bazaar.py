import os


class InsufficientStockError(Exception):
    pass


def load_from_file(filename):
    inventory = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    name, price, quantity = line.strip().split(",")
                    inventory.append({
                        "name": name,
                        "price": float(price),
                        "quantity": int(quantity)
                    })
                except:
                    continue
    except FileNotFoundError:
        return []
    return inventory


def save_to_file(inventory, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in inventory:
            f.write(f"{item['name']},{item['price']},{item['quantity']}\n")


def add_product(inventory, name, price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError

    for item in inventory:
        if item["name"] == name:
            item["quantity"] += quantity
            item["price"] = price
            return

    inventory.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })


def sell_product(inventory, name, quantity):
    for item in inventory:
        if item["name"] == name:
            if item["quantity"] < quantity:
                raise InsufficientStockError
            item["quantity"] -= quantity
            return
    raise ValueError
