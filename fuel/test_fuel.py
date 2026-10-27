import pytest
from fuel import convert, gauge


def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("1/100") == 1


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3.5/4")
    with pytest.raises(ValueError):
        convert("5/3")


def test_gauge_E():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percent():
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
