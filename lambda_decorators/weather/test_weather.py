import pytest
from weather import describe_weather, classifier

def test_hot():
    assert describe_weather(30) == "hot"

def test_warm():
    assert describe_weather(20) == "warm"

def test_cold():
    assert describe_weather(-5) == "cold"

def test_invalid_high():
    with pytest.raises(ValueError, match="Invalid temperature"):
        describe_weather(100)

def test_invalid_low():
    with pytest.raises(ValueError):
        describe_weather(-100)

def test_classifier_boundaries():
    assert classifier(10) == "warm"
    assert classifier(25) == "hot"
    assert classifier(9)  == "cold"