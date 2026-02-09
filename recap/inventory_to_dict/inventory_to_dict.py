def inventory_to_dict(inventory_list):
    result = {}
    for item in inventory_list:
        pid, name, price, cat = item
        result[pid] = {"name": name, "price": price, "category": cat}
    return result

def main():
    inventory_list = [["P001", "Test Product", 99, "Test"]]
    result = inventory_to_dict(inventory_list)
    print(result)

if __name__ == "__main__":
    main()