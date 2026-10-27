# CS50P Week7
from um import count


def test_count_expectedText():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("!!! hehe, UM!! djie") == 1
    assert count("mummy eatum _um rice ") == 0


def test_count_unexceptedText():
    assert count("balala!") == 0
    assert count("123um123") == 0
    assert count("inevitable game") == 0
