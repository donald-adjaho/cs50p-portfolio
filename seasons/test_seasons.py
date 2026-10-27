import pytest
from seasons import convert_time_left


def test_expected_birthDate():
    assert convert_time_left("2014-01-01")
    assert convert_time_left("2004-01-02")


def test_unexpected_birthDate():
    with pytest.raises(ValueError):
        convert_time_left("19 January, 2014")
    with pytest.raises(ValueError):
        convert_time_left("2019-1-02")
    with pytest.raises(ValueError):
        convert_time_left("2010-01-2")
    with pytest.raises(ValueError):
        convert_time_left("2020-12-32")
