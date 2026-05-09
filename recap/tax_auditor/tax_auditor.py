def calculate_tax(category, price):
    if category == "Food":
         tax = (5/100)*price
         return tax
    elif category == "Electronics":
         tax = (20/100)*price
         return tax
    else:
         tax = (10/100)*price
         return tax


def process_sales(data_list):
    sales_dict = {}
    for item in data_list:
        transaction_id, product_name, category, base_price = item
        tax = calculate_tax(category, base_price)
        sales_dict [transaction_id] = {
            "name": product_name,
            "total_price": base_price + tax,
            "is_premium": base_price + tax > 500
        }
    return sales_dict



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
