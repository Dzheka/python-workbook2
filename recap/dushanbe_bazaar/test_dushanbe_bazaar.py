import pytest
import os
from dushanbe_bazaar import load_from_file, save_to_file, add_product, sell_product, InsufficientStockError


@pytest.fixture
def temp_inventory_file(tmp_path):
    return str(tmp_path / "test_bazaar.txt")


def test_load_non_existent_file():
    assert load_from_file("ghost.txt") == []


def test_save_and_load_file(temp_inventory_file):
    inventory = [{"name": "Qurut", "price_tjs": 1.5, "quantity": 200}]
    save_to_file(inventory, temp_inventory_file)

    loaded = load_from_file(temp_inventory_file)
    assert len(loaded) == 1
    assert loaded[0]["name"] == "Qurut"
    assert loaded[0]["quantity"] == 200


def test_load_corrupted_lines(temp_inventory_file):
    # Creating a file with one good line and one bad line
    with open(temp_inventory_file, 'w') as f:
        f.write("Honey,80,5\n")
        f.write("BrokenLineWithNoCommas\n")
        f.write("InvalidPrice,text_here,10\n")

    loaded = load_from_file(temp_inventory_file)
    assert len(loaded) == 1
    assert loaded[0]["name"] == "Honey"


def test_add_product_error():
    with pytest.raises(ValueError):
        add_product([], "Lemon", -5, 10)


def test_sell_stock_error():
    inventory = [{"name": "Jurabs", "price_tjs": 40, "quantity": 5}]
    with pytest.raises(InsufficientStockError):
        sell_product(inventory, "Jurabs", 10)


def test_sell_not_found_error():
    inventory = [{"name": "Jurabs", "price_tjs": 40, "quantity": 5}]
    with pytest.raises(ValueError, match="not found"):
        sell_product(inventory, "Apples", 1)
