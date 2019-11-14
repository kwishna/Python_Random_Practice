import unittest
from Calc import Calculator

class UnitTest(unittest.TestCase):

    calc = Calculator()

    def test_one(self):
        
        result = UnitTest.calc.add(1, 3)
        self.assertEqual(result, 4, "Summation Is Failed")

    def test_two(self):
        
        result = UnitTest.calc.subtract(1, 3)
        self.assertEqual(result, -2, "Subtraction Is Failed")

    def test_three(self):
        
        result = UnitTest.calc.mul(1, 3)
        self.assertEqual(result, 3, "Multiplication Is Failed")

if __name__ == '__main__':
    unittest.main(verbosity=3)