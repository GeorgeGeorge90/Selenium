import pytest


def add_two_numbers(a, b):
    return a + b


@pytest.mark.test
def test_small_numbers():
    assert add_two_numbers(1, 2) == 3, "The sum should be 3"


@pytest.mark.test
def test_large_numbers():
    assert add_two_numbers(100, 200) != 300, "The sum should be 300"
