from bank import value


def test_hello_greeting():
    assert value("hello") == 0
    assert value("Hello, guy!") == 0
    assert value("HELLO, friend") == 0


def test_h_but_not_hello():
    assert value("hi, brother!!") == 20
    assert value("Hey you") == 20


def test_other_greetings():
    assert value("Good morning") == 100
    assert value("yo what's up") == 100
    assert value("bonjour") == 100


def test_case_insensitivity():
    assert value("HeLLo!") == 0
    assert value("hEy") == 20
    assert value("HELLO WORLD") == 0
