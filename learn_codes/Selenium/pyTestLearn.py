import pytest

def fun(var):
    return var + 1

def test_success():
    assert fun(5) == 6

def test_fail():
    assert fun(5) == 6

def test_one():
    assert fun(6) == 7
