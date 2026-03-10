import types
from amazon import affordable, best_rated, total_price

PRODUCTS = [
    {"name": "Laptop",  "price": 1200, "rating": 4.5},
    {"name": "Phone",   "price": 800,  "rating": 4.8},
    {"name": "Headset", "price": 150,  "rating": 3.9},
    {"name": "Tablet",  "price": 600,  "rating": 4.2},
    {"name": "Cable",   "price": 10,   "rating": 3.5},
]

def test_affordable_is_generator():
    assert isinstance(affordable(PRODUCTS, 700), types.GeneratorType)

def test_affordable_excludes_expensive():
    names = [p["name"] for p in affordable(PRODUCTS, 700)]
    assert "Laptop" not in names

def test_affordable_includes_cheap():
    names = [p["name"] for p in affordable(PRODUCTS, 700)]
    assert "Headset" in names
    assert "Cable" in names

def test_best_rated():
    assert best_rated(PRODUCTS)["name"] == "Phone"

def test_total_price():
    assert total_price(PRODUCTS) == 2760

def test_total_price_empty():
    assert total_price([]) == 0