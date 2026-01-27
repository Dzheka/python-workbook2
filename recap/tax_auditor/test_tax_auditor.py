from tax_auditor import calculate_tax, process_sales


def test_calculate_tax_food():
    assert calculate_tax("Food", 100.0) == 5.0
    assert calculate_tax("Food", 2.0) == 0.1


def test_calculate_tax_electronics():
    assert calculate_tax("Electronics", 1000.0) == 200.0
    assert calculate_tax("Electronics", 150.0) == 30.0


def test_calculate_tax_other():
    assert calculate_tax("Clothing", 100.0) == 10.0
    assert calculate_tax("Books", 50.0) == 5.0


def test_process_sales_empty():
    raw_sales = []
    result = process_sales(raw_sales)
    assert result == {}


def test_process_sales_single_food():
    raw_sales = [["T1", "Bread", "Food", 2.0]]
    result = process_sales(raw_sales)

    assert result == {
        "T1": {
            "name": "Bread",
            "total_price": 2.1,
            "is_premium": False
        }
    }


def test_process_sales_single_premium():
    raw_sales = [["T2", "Laptop", "Electronics", 1200.0]]
    result = process_sales(raw_sales)

    assert result == {
        "T2": {
            "name": "Laptop",
            "total_price": 1440.0,
            "is_premium": True
        }
    }


def test_process_sales_boundary_premium():
    # Test boundary: exactly 500 should not be premium
    raw_sales = [["T1", "Item", "Other", 500.0]]
    result = process_sales(raw_sales)
    assert result["T1"]["total_price"] == 550.0
    assert result["T1"]["is_premium"] == True

    # Test just below premium threshold
    raw_sales = [["T2", "Item", "Food", 476.19]]
    result = process_sales(raw_sales)
    assert result["T2"]["total_price"] == 499.9995
    assert result["T2"]["is_premium"] == False


def test_process_sales_full_dataset():
    raw_sales = [
        ["T1", "Bread", "Food", 2.0],
        ["T2", "Laptop", "Electronics", 1200.0],
        ["T3", "Apple", "Food", 1.5],
        ["T4", "Headphones", "Electronics", 150.0],
        ["T5", "Monitor", "Electronics", 300.0],
        ["T6", "T-shirt", "Clothing", 40.0]
    ]

    result = process_sales(raw_sales)

    assert len(result) == 6

    assert result["T1"]["name"] == "Bread"
    assert result["T1"]["total_price"] == 2.1
    assert result["T1"]["is_premium"] == False

    assert result["T2"]["name"] == "Laptop"
    assert result["T2"]["total_price"] == 1440.0
    assert result["T2"]["is_premium"] == True

    assert result["T3"]["name"] == "Apple"
    assert result["T3"]["total_price"] == 1.575
    assert result["T3"]["is_premium"] == False

    assert result["T4"]["name"] == "Headphones"
    assert result["T4"]["total_price"] == 180.0
    assert result["T4"]["is_premium"] == False

    assert result["T5"]["name"] == "Monitor"
    assert result["T5"]["total_price"] == 360.0
    assert result["T5"]["is_premium"] == False

    assert result["T6"]["name"] == "T-shirt"
    assert result["T6"]["total_price"] == 44.0
    assert result["T6"]["is_premium"] == False


def test_process_sales_all_premium():
    raw_sales = [
        ["T1", "Server", "Electronics", 5000.0],
        ["T2", "Workstation", "Electronics", 3000.0]
    ]

    result = process_sales(raw_sales)

    assert result["T1"]["is_premium"] == True
    assert result["T2"]["is_premium"] == True
