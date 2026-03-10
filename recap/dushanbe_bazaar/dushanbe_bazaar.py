class InsufficientStockError(Exception):
    pass


def load_from_file(filename):
    inventory = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                try:
                    inventory.append({
                        "name": parts[0],
                        "price_tjs": float(parts[1]),
                        "quantity": int(parts[2])
                    })
                except ValueError:
                    continue
    except FileNotFoundError:
        return []
    return inventory


def save_to_file(inventory, filename):
    with open(filename, "w") as f:
        for item in inventory:
            f.write(f"{item['name']},{item['price_tjs']},{item['quantity']}\n")


def add_product(inventory, name, price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must not be negative")
    for item in inventory:
        if item["name"] == name:
            item["price_tjs"] = price
            item["quantity"] += quantity
            return inventory
    inventory.append({"name": name, "price_tjs": price, "quantity": quantity})
    return inventory


def sell_product(inventory, name, quantity):
    for item in inventory:
        if item["name"] == name:
            if item["quantity"] < quantity:
                raise InsufficientStockError("Not enough stock")
            item["quantity"] -= quantity
            return inventory
    raise ValueError(f"{name} not found")
