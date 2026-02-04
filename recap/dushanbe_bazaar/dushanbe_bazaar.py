class InsufficientStockError(Exception):
    pass


def load_from_file(filename):
    inventory = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, price_str, qty_str = line.split(",")
                    inventory.append({
                        "name": name,
                        "price": float(price_str),
                        "quantity": int(qty_str)
                    })
                except ValueError:
                    continue
    except FileNotFoundError:
        return []

    return inventory


def save_to_file(inventory, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in inventory:
            f.write(f"{item['name']},{item['price']},{item['quantity']}\n")


def add_product(inventory, name, price, quantity):
    price = float(price)
    quantity = int(quantity)

    if price < 0 or quantity < 0:
        raise ValueError

    for item in inventory:
        if item["name"] == name:
            item["quantity"] += quantity
            return

    inventory.append({"name": name, "price": price, "quantity": quantity})


def sell_product(inventory, name, quantity):
    quantity = int(quantity)
    if quantity < 0:
        raise ValueError

    for item in inventory:
        if item["name"] == name:
            if item["quantity"] < quantity:
                raise InsufficientStockError
            item["quantity"] -= quantity
            return

    raise ValueError


if __name__ == "__main__":
    inv = load_from_file("inventory.txt")
    add_product(inv, "Khujand Lemons", 15.5, 5)
    sell_product(inv, "Khujand Lemons", 2)
    save_to_file(inv, "inventory.txt")
    print(inv)
