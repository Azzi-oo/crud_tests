import pytest


def calc(num_a, num_b, operation):
    return eval(str(num_a) + operation + str(num_b))


@pytest.mark.parametrize(
    "num_a, num_b, operation, expected",
    [(2, 2, "+", 4),
     (2, 2, "-", 0),
     (2, 2, "*", 4),
     (2, 2, "/", 1)])
def test_eval(num_a, num_b, operation, expected):
    assert calc(num_a, num_b, operation) == expected


@pytest.mark.parametrize("num_a, num_b, operation, expected", [pytest.param("2", "2", "+", 4, marks=pytest.mark.xfail)])
def test_eval(num_a, num_b, operation, expected):
    assert calc(num_a, num_b, operation) == expected
