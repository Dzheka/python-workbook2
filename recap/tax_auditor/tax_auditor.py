def calculate_tax(cat, price):
    if cat == "Food":
        return price * 0.05
    elif cat == "Electronics":
        return price * 0.20
    else:
        return price * 0.10

def process_sales(data_list):
    result = {}
    for t in data_list:
        tid, name, cat, price = t
        tax = calculate_tax(cat, price)
        total = price + tax
        premium = total > 500
        result[tid] = {
            "name": name,
            "total_price": total,
            "is_premium": premium
        }
    return result

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