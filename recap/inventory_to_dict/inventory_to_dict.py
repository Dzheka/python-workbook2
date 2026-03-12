def inventory_to_dict(inventory_list):
    inventory_dict = {}

    for product_id, name, price, category in inventory_list:
        inventory_dict[product_id] = {
            "name": name,
            "price": price,
            "category": category,
        }

    return inventory_dict
