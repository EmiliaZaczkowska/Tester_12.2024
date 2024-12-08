from cw2_kod import *


def test_multiply_integer():
    assert multiply(2, 5) == 10
    assert multiply(3, 1) == 3
    assert multiply(7, 3) == 21

def test_multiply_float():
    assert multiply(100, 1.1) == 110
    assert multiply(5, 3.5) == 17.5
    assert multiply(3, 1.5) == 4.5
    assert multiply(3, 3.3333) == 9.9999
def test_multiply_small():
    assert multiply(0.01, 0.03) == 0.0003

def test_multiply_string():
    assert multiply("5", "3") == 15

def test_multiply_string_not_to_int():
    assert multiply("4.6", "swieta") == None





