def inventory_to_dict(inventory_list):
  bigdict = dict()
  for i in range(len(inventory_list)):
    dic = dict()
    each = inventory_list[i]
    code = each[0]
    dic["name"] = each[1]
    dic["price"] = each[2]
    dic["category"] = each[3]
    bigdict[code] = dic
  return bigdict


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
