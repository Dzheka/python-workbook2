def calculate_tax(category, price: int):
    if category == "Food":
        return price*21/20
    elif category == "Electronics":
        return price*6/5
    else:
        return price*11/10

def process_sales(data_list):
    big = dict()
    for i in range (len(data_list)):
      each = data_list[i]
      category = each[2]
      price = each[3]
      small = dict()
      small["name"] = each[1]
      small["total_price"] = calculate_tax(category,price)
      if small["total_price"] > 500:
        small["is_premium"] = True
      else:
        small["is_premium"] = False
      ID = each[0]
      big[ID] = small
    return big




def main():
    raw_sales = [
        ["T1", "Bread", "Food", 2.0],
        ["T2", "Laptop", "Electronics", 1200.0],
        ["T3", "Apple", "Food", 1.5],
        ["T4", "Headphones", "Electronics", 150.0],
        ["T5", "Monitor", "Electronics", 300.0],
        ["T6", "T-shirt", "Clothing", 40.0]
    ]

    result = process_sales(raw_sales)
    print(result)


if __name__ == "__main__":
    main()
