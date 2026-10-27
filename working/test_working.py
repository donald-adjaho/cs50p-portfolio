from working import convert
import pytest


def test_convert_expectedInput():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM")
    assert convert("10 AM to 8:50 PM")
    assert convert("10:30 PM to 8 AM")


def test_convert_unexpectedInput():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
        convert("9 AM - 5 PM")
        convert("cat")
        convert("")


def test_convert_missingMinutes():
    with pytest.raises(ValueError):
        convert("10: AM to 12:30 PM")
        convert("10:30 AM to 11: AM")


def test_convert_missingHours():
    with pytest.raises(ValueError):
        convert(":30 AM to 12:35 PM")
        convert("11:30 PM to 09: AM")


def test_convert_missing_AM_PM():
    with pytest.raises(ValueError):
        convert("5:30 to 6:30")
        convert("6:00 PM to 9:30")
        convert("6:00 to 9:30 AM")


def test_convert_omitting_to():
    with pytest.raises(ValueError):
        convert("09:00 AM 17:00 PM")
        convert("09:00 AM 17: 00 PM")


def test_convert_outRange_time():
    with pytest.raises(ValueError):
        convert("13 AM to 14 PM")
        convert("14 AM to 13 PM")
