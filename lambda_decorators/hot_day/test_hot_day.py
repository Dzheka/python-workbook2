import types
from hot_day import hot_days, first_n_hot

DATA = [("Mon", 28), ("Tue", 35), ("Wed", 31), ("Thu", 22), ("Fri", 33)]

def test_hot_days_is_generator():
    assert isinstance(hot_days(DATA), types.GeneratorType)

def test_hot_days_correct():
    assert list(hot_days(DATA)) == [("Tue", 35), ("Wed", 31), ("Fri", 33)]

def test_hot_days_none():
    assert list(hot_days([("Mon", 20), ("Tue", 15)])) == []

def test_first_n_hot():
    assert first_n_hot(DATA, 2) == [("Tue", 35), ("Wed", 31)]

def test_first_n_hot_more_than_available():
    assert first_n_hot(DATA, 10) == [("Tue", 35), ("Wed", 31), ("Fri", 33)]