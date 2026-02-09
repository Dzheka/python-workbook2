import os

class InsufficientStockError(Exception):
    pass

def load_from_file(filename):
    inv = []
    if not os.path.exists(filename):
        return inv
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            name, price, qty = parts
            try:
                price = float(price)
                qty = int(qty)
                inv.append({"name": name, "price": price, "quantity": qty})
            except:
                continue
    return inv

def save_to_file(inv, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in inv:
            f.write(f"{item['name']},{item['price']},{item['quantity']}\n")

def add_product(inv, name, price, qty):
    if price < 0 or qty < 0:
        raise ValueError("Negative values not allowed")
    for item in inv:
        if item["name"] == name:
            item["quantity"] += qty
            return
    inv.append({"name": name, "price": price, "quantity": qty})

def sell_product(inv, name, qty):
    for item in inv:
        if item["name"] == name:
            if item["quantity"] < qty:
                raise InsufficientStockError("Not enough stock")
            item["quantity"] -= qty
            return
    raise ValueError("Product not found")