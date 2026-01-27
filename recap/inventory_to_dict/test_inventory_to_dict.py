from inventory_to_dict import inventory_to_dict


def test_empty_list():
    inventory_list = []
    result = inventory_to_dict(inventory_list)
    assert result == {}


def test_single_item():
    inventory_list = [["P001", "Test Product", 99, "Test"]]
    result = inventory_to_dict(inventory_list)

    assert result == {
        "P001": {"name": "Test Product", "price": 99, "category": "Test"}
    }


def test_two_items():
    inventory_list = [
        ["P104", "Dell XPS 15", 2000, "Laptops"],
        ["P105", "Mechanical Keyboard", 150, "Accessories"]
    ]
    result = inventory_to_dict(inventory_list)

    assert result == {
        "P104": {"name": "Dell XPS 15", "price": 2000, "category": "Laptops"},
        "P105": {"name": "Mechanical Keyboard", "price": 150, "category": "Accessories"}
    }


def test_basic_inventory():
    inventory_list = [
        ["P101", "MacBook Pro", 2500, "Laptops"],
        ["P102", "iPhone 15", 1000, "Phones"],
        ["P103", "AirPods Pro", 250, "Accessories"]
    ]
    result = inventory_to_dict(inventory_list)

    assert result == {
        "P101": {"name": "MacBook Pro", "price": 2500, "category": "Laptops"},
        "P102": {"name": "iPhone 15", "price": 1000, "category": "Phones"},
        "P103": {"name": "AirPods Pro", "price": 250, "category": "Accessories"}
    }


def test_full_inventory():
    inventory_list = [
        ["P101", "MacBook Pro", 2500, "Laptops"],
        ["P102", "iPhone 15", 1000, "Phones"],
        ["P103", "AirPods Pro", 250, "Accessories"],
        ["P104", "Dell XPS 15", 2000, "Laptops"],
        ["P105", "Mechanical Keyboard", 150, "Accessories"]
    ]
    result = inventory_to_dict(inventory_list)

    assert len(result) == 5
    assert result["P101"]["name"] == "MacBook Pro"
    assert result["P102"]["price"] == 1000
    assert result["P103"]["category"] == "Accessories"
    assert result["P104"]["name"] == "Dell XPS 15"
    assert result["P105"]["price"] == 150
