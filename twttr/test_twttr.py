from twttr import shorten


def test_upper_shorten():
    assert shorten("TWITTER") == "TWTTR"


def test_lower_shorten():
    assert shorten("what's your name ?") == "wht's yr nm ?"


def test_capit_shorten():
    assert shorten("Elephant") == "lphnt"


def test_ommit_number():
    assert shorten("1_shut up now123") == "1_sht p nw123"
