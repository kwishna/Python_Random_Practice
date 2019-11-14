import pytest


def test_me(cache):
    print("Krishna Kumar Singh", cache)
    assert True
#
# def f():
#     raise SystemExit(1)
#
#
# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()

# #########################################
# content of test_class.py
# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "h" in x
#
#     def test_two(self):
#         x = "hello"
#         assert hasattr(x, "check")