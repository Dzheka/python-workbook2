class InsufficientStockError(Exception):
    pass

def load_from_file(filename):
    inventory = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, price_str, quantity_str = line.split(',')
                    price = float(price_str)
                    quantity = int(quantity_str)
                    inventory.append({'name': name, 'price': price, 'quantity': quantity})
                except (ValueError, IndexError):
                    continue
    except FileNotFoundError:
        return []
    return inventory

def save_to_file(inventory, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for product in inventory:
            line = f"{product['name']},{product['price']},{product['quantity']}\n"
            f.write(line)

def add_product(inventory, name, price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative")

    for product in inventory:
        if product['name'] == name:
            product['quantity'] += quantity
            return

    inventory.append({'name': name, 'price': price, 'quantity': quantity})

def sell_product(inventory, name, quantity):
    for product in inventory:
        if product['name'] == name:
            if product['quantity'] < quantity:
                raise InsufficientStockError(f"Not enough stock of {name}. Available: {product['quantity']}, requested: {quantity}")
            product['quantity'] -= quantity
            return
    raise ValueError(f"Product {name} not found in inventory")
