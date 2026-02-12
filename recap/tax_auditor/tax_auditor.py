def calculate_tax(category, price):
    if category == "Food":
        return price * 0.05
    elif category == "Electronics":
        return price * 0.20
    else:
        return price * 0.10


def process_sales(data_list):
    result = {}

    for transaction_id, name, category, base_price in data_list:
        tax = calculate_tax(category, base_price)
        total_price = base_price + tax
        is_premium = total_price > 500

        result[transaction_id] = {
            "name": name,
            "total_price": total_price,
            "is_premium": is_premium,
        }

    return result
