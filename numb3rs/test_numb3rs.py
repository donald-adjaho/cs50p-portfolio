from numb3rs import validate


def test_validate():
    assert validate("255.255.255.255")
    assert validate("128.200.235.7")
    assert validate("128.0.0.1")


def test_validate_frontString():
    assert not validate("cat.255.255.255")
    assert not validate("855.345.45")


def test_validate_notIp():
    assert not validate("belivery")


def test_validate_firstbyte():
    assert not validate("255.500.600.700")
