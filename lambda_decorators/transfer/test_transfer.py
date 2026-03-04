import pytest
from transfer import transfer

def test_transfer_returns_amount():
    assert transfer(500) == 500

def test_transfer_returns_zero():
    assert transfer(0) == 0

def test_transfer_returns_negative():
    assert transfer(-100) == -100

def test_decorator_preserves_return_value():
    assert transfer(250) == 250

def test_decorator_prints_output(capsys):
    transfer(100)
    captured = capsys.readouterr()
    assert "Transaction started" in captured.out
    assert "Transaction finished: 100" in captured.out