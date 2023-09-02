import pytest
from fibonacci import fibo


def test_fibo_8():
    assert (fibo(8) == [0, 1, 1, 2, 3, 5, 8, 13])