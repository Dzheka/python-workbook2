def inventory_to_dict(inventory_list):
    return {
        item[0]: {
            "name": item[1],
            "price": item[2],
            "category": item[3]
        }
        for item in inventory_list
    }


def main():
    inventory_list = [
        ["P101", "MacBook Pro", 2500, "Laptops"],
        ["P102", "iPhone 15", 1000, "Phones"],
        ["P103", "AirPods Pro", 250, "Accessories"],
        ["P104", "Dell XPS 15", 2000, "Laptops"],
        ["P105", "Mechanical Keyboard", 150, "Accessories"]
    ]

    result = inventory_to_dict(inventory_list)
    print(result)


if __name__ == "__main__":
    main()
