from compound_interest import compound_interest

def test_zero_years():
    assert compound_interest(1000, 0.1, 0) == 1000.0

def test_one_year():
    assert compound_interest(1000, 0.1, 1) == 1100.0

def test_three_years():
    assert compound_interest(1000, 0.1, 3) == 1331.0

def test_two_years_float_rate():
    assert compound_interest(500, 0.05, 2) == 551.25

def test_zero_rate():
    assert compound_interest(1000, 0.0, 5) == 1000.0