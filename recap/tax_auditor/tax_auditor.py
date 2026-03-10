def calculate_tax(category, price):
    if category == "Food":
        return price * 0.05
    elif category == "Electronics":
        return price * 0.20
    else:
        return price * 0.10

def process_sales(data_list):
    results = {}

    for item in data_list:
        t_id, name, category, price = item

        tax_amount = calculate_tax(category, price)
        total_price = price + tax_amount
        is_premium = total_price > 500

        results[t_id] = {
            "name": name,
            "total_price": total_price,
            "is_premium": is_premium
        }

    return results

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
