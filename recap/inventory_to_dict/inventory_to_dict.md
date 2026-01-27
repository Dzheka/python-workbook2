# Inventory List to Dictionary

Convert an inventory list (list of lists) into a dictionary where the product ID is the key and the remaining information forms a nested dictionary.

## Input
A list of lists where each inner list contains:
- Product ID (string)
- Product name (string)
- Price (number)
- Category (string)

## Output
A dictionary where:
- Key: Product ID
- Value: Dictionary with keys "name", "price", "category"

## Examples

### Example 1
```python
inventory_list = [
    ["P101", "MacBook Pro", 2500, "Laptops"],
    ["P102", "iPhone 15", 1000, "Phones"],
    ["P103", "AirPods Pro", 250, "Accessories"]
]

result = inventory_to_dict(inventory_list)
print(result)
# {
#     "P101": {"name": "MacBook Pro", "price": 2500, "category": "Laptops"},
#     "P102": {"name": "iPhone 15", "price": 1000, "category": "Phones"},
#     "P103": {"name": "AirPods Pro", "price": 250, "category": "Accessories"}
# }
```

### Example 2
```python
inventory_list = [
    ["P104", "Dell XPS 15", 2000, "Laptops"],
    ["P105", "Mechanical Keyboard", 150, "Accessories"]
]

result = inventory_to_dict(inventory_list)
print(result)
# {
#     "P104": {"name": "Dell XPS 15", "price": 2000, "category": "Laptops"},
#     "P105": {"name": "Mechanical Keyboard", "price": 150, "category": "Accessories"}
# }
```

### Example 3
```python
inventory_list = []
result = inventory_to_dict(inventory_list)
print(result)  # {}
```
