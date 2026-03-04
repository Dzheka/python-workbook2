from shopping_cart import ShoppingCart

def test_total_no_discount():
    cart = ShoppingCart("Alice")
    cart.add({"name": "Book", "price": 20}, {"name": "Pen", "price": 5})
    assert cart.total() == 25

def test_total_with_discount():
    cart = ShoppingCart("Alice")
    cart.add({"name": "Book", "price": 20}, {"name": "Pen", "price": 5})
    assert cart.total(Book=50) == 15.0

def test_add_multiple():
    cart = ShoppingCart("Bob")
    cart.add({"name": "A", "price": 10}, {"name": "B", "price": 10})
    assert len(cart.items) == 2

def test_summary():
    cart = ShoppingCart("Alice")
    cart.add({"name": "Book", "price": 20})
    s = cart.summary()
    assert s["owner"] == "Alice"
    assert "Book" in s["items"]
    assert s["total"] == 20

def test_empty_cart():
    cart = ShoppingCart("Alice")
    assert cart.total() == 0