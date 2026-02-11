def inventory_to_dict(inventory_list):
    result = {}
    for product_id, name, price, category in inventory_list:
        result[product_id] = {
            "name": name,
            "price": price,
            "category": category
        }
    return result


if __name__ == "__main__":
    inventory_list = [
        ["P101", "MacBook Pro", 2500, "Laptops"],
        ["P102", "iPhone 15", 1000, "Phones"],
        ["P103", "AirPods Pro", 250, "Accessories"]
    ]
    print(inventory_to_dict(inventory_list))

    inventory_list = [
        ["P104", "Dell XPS 15", 2000, "Laptops"],
        ["P105", "Mechanical Keyboard", 150, "Accessories"]
    ]
    print(inventory_to_dict(inventory_list))

    inventory_list = []
    print(inventory_to_dict(inventory_list))
