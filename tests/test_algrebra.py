from morning_ci.algebra import addititon


def test_addition_1():
    assert addititon(1, 1) == 2


def test_addition_2():
    assert addititon(-1, -1) == -2
