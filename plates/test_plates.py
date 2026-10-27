from plates import is_valid


def test_valid_plate():
    assert is_valid("CS50")
    assert is_valid("AB123")


def test_starts_with_two_letters():
    assert not is_valid("1ABC")
    assert not is_valid("C5")


def test_invalid_characters():
    assert not is_valid("AB CD")
    assert not is_valid("CS@50")


def test_max_length():
    assert not is_valid("CS12345")
    assert not is_valid("ABCDEFG")


def test_leading_zero_in_number():
    assert not is_valid("CS05")


def test_number_middle_string():
    assert not is_valid("CS50PR")
