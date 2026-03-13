def calculate_tax(category, price):
    if category == "Food":
        return round(price * 0.05, 2)
    elif category == "Electronics":
        return round(price * 0.20, 2)
    else:
        return round(price * 0.10, 2)


def process_sales(data_list):
    result = {}

    for item in data_list:
        transaction_id, name, category, base_price = item
        tax = calculate_tax(category, base_price)
        total_price = round(base_price + tax, 2)
        is_premium = total_price > 500

        result[transaction_id] = {
            "name": name,
            "total_price": total_price,
            "is_premium": is_premium,
        }

    return result


def main():
    raw_sales = [
        ["T1", "Bread", "Food", 2.0],
        ["T2", "Laptop", "Electronics", 1200.0],
        ["T3", "Apple", "Food", 1.5],
        ["T4", "Headphones", "Electronics", 150.0],
        ["T5", "Monitor", "Electronics", 300.0],
        ["T6", "T-shirt", "Clothing", 40.0],
    ]

    result = process_sales(raw_sales)
    for tid, info in result.items():
        print(f"{tid}: {info}")


if __name__ == "__main__":
    main()
