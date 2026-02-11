def calculate_tax(category, price):
    if category == "Food":
        return price * 0.05
    if category == "Electronics":
        return price * 0.2
    return price * 0.1


def process_sales(data_list):
    result = {}
    for transaction_id, name, category, base_price in data_list:
        tax = calculate_tax(category, base_price)
        total_price = base_price + tax
        is_premium = total_price > 500
        result[transaction_id] = {
            "name": name,
            "total_price": total_price,
            "is_premium": is_premium
        }
    return result


if __name__ == "__main__":
    raw_sales = [
        ["T1", "Bread", "Food", 2.0],
        ["T2", "Laptop", "Electronics", 1200.0],
        ["T3", "Apple", "Food", 1.5],
        ["T4", "Headphones", "Electronics", 150.0],
        ["T5", "Monitor", "Electronics", 300.0],
        ["T6", "T-shirt", "Clothing", 40.0]
    ]
    print(process_sales(raw_sales)["T2"])

    raw_sales = [
        ["T1", "Bread", "Food", 2.0]
    ]
    print(process_sales(raw_sales))

    raw_sales = []
    print(process_sales(raw_sales))
