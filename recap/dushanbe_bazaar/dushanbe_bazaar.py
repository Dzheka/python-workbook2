class InsufficientStockError(Exception):
    """Custom exception for insufficient stock"""
    pass


def load_from_file(filename):
    """Read inventory from file and return list of dictionaries"""
    inventory = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    line = line.strip()
                    if not line:  # Skip empty lines
                        continue

                    parts = line.split(',')
                    if len(parts) != 3:
                        continue  # Skip malformed lines

                    name = parts[0].strip()
                    price = float(parts[1].strip())
                    quantity = int(parts[2].strip())

                    inventory.append({
                        'name': name,
                        'price_tjs': price,
                        'quantity': quantity
                    })
                except (ValueError, IndexError):
                    # Skip lines with invalid data
                    continue
    except FileNotFoundError:
        return []

    return inventory


def save_to_file(inventory, filename):
    """Write inventory list to file"""
    with open(filename, 'w', encoding='utf-8') as file:
        for item in inventory:
            # Handle both 'price' and 'price_tjs' keys
            price = item.get('price_tjs', item.get('price', 0))
            file.write(f"{item['name']},{price},{item['quantity']}\n")


def add_product(inventory, name, price, quantity):
    """Add or update product in inventory"""
    if price < 0:
        raise ValueError("Price cannot be negative")
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    # Check if product exists
    for item in inventory:
        if item['name'] == name:
            item['quantity'] += quantity
            return

    # Add new product
    inventory.append({
        'name': name,
        'price_tjs': price,
        'quantity': quantity
    })


def sell_product(inventory, name, quantity):
    """Sell product from inventory"""
    for item in inventory:
        if item['name'] == name:
            if item['quantity'] < quantity:
                raise InsufficientStockError(
                    f"Not enough stock for {name}. Available: {item['quantity']}, Requested: {quantity}"
                )
            item['quantity'] -= quantity
            return

    raise ValueError(f"Product '{name}' not found in inventory")