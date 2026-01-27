# The Smart Tax Auditor

Calculate taxes and categorize transactions as premium or regular based on total price.

## Input
A list of lists where each inner list contains:
- Transaction ID (string)
- Product name (string)
- Category (string)
- Base price (float)

## Tasks

### Part 1: Tax Calculator
Create a function `calculate_tax(category, price)` that returns the tax amount:
- If category is "Food", tax is 5% of the price
- If category is "Electronics", tax is 20% of the price
- For any other category, tax is 10% of the price

### Part 2: Sales Processor
Create a function `process_sales(data_list)` that:
- Iterates through the raw_sales list
- Calls `calculate_tax()` to get the tax for each item
- Calculates `total_price` (base price + tax)
- Determines `is_premium`: True if total_price > 500, otherwise False
- Returns a dictionary where the key is Transaction_ID and value contains:
  - `name`: product name
  - `total_price`: base price + tax
  - `is_premium`: boolean value

## Examples

### Example 1
```python
raw_sales = [
    ["T1", "Bread", "Food", 2.0],
    ["T2", "Laptop", "Electronics", 1200.0],
    ["T3", "Apple", "Food", 1.5],
    ["T4", "Headphones", "Electronics", 150.0],
    ["T5", "Monitor", "Electronics", 300.0],
    ["T6", "T-shirt", "Clothing", 40.0]
]

result = process_sales(raw_sales)
print(result["T2"])
# {
#     "name": "Laptop",
#     "total_price": 1440.0,
#     "is_premium": True
# }
```

### Example 2
```python
raw_sales = [
    ["T1", "Bread", "Food", 2.0]
]

result = process_sales(raw_sales)
print(result)
# {
#     "T1": {
#         "name": "Bread",
#         "total_price": 2.1,
#         "is_premium": False
#     }
# }
```

### Example 3
```python
raw_sales = []
result = process_sales(raw_sales)
print(result)  # {}
```
