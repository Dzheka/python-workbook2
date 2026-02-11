def calculate_tax(category, price):
    if category == "Food":
        return price * 0.05
    if category == "Electronics":
        return price * 0.2
    return price * 0.1


def process_sales(data_list):
        if data_list == []:
            return {}
        result = {}
        for i in range (len(data_list)):
             tax = calculate_tax(data_list[i][2], data_list[i][3])
             total_price = data_list[i][3]  + tax
             result[data_list[i][0]] = {
                 "name" : data_list[i][1],
                 "total_price" : total_price,
                 "is_premium" : total_price>500
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
