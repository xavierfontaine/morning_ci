from morning_ci.algebra import addititon


def test_addition_1():
    addititon(1, 1) == 2


def test_addition_2():
    addititon(-1, -1) == -2
