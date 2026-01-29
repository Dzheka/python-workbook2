# Assignment: Dushanbe Bazaar - Text File Manager 📦🍎

You are managing a warehouse in Dushanbe using a simple text-based database (`inventory.txt`). Each line in the file stores a product in the following format:
`Product Name,Price_TJS,Quantity`

### Requirements:

1.  **File Format**: Example of `inventory.txt`:
    ```text
    Khujand Lemons,15.5,100
    Pamir Jurabs,45.0,20
    ```

2.  **`load_from_file(filename)`**:
    - Read the file and return a list of dictionaries.
    - **Error Handling**: 
        - If the file doesn't exist, return an empty list.
        - Use `try-except` to skip lines that are formatted incorrectly (e.g., missing a comma or having text where a number should be).

3.  **`save_to_file(inventory, filename)`**:
    - Write the list of dictionaries back into the text file in the `Name,Price,Quantity` format.

4.  **`add_product(inventory, name, price, quantity)`**:
    - Validation: Raise a `ValueError` if price or quantity is negative.
    - If the product exists, update its quantity.

5.  **`sell_product(inventory, name, quantity)`**:
    - Raise a `ValueError` if the product is missing.
    - Raise a custom `InsufficientStockError` if there isn't enough stock.