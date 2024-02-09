import unittest
from app import square_root, factorial, natural_logarithm, power

class CalculatorTest(unittest.TestCase):
    def test_sqrt(self):
        result = square_root(100)
        self.assertEqual(result, 10)

    def test_fact(self):
        result = factorial(6)
        self.assertEqual(result, 720)

    def test_ln(self):
        result = natural_logarithm(10)
        self.assertEqual(round(result, 6), 2.302585)
    
    def test_power(self):
        result = power(2, 10)
        self.assertEqual(result, 1024)
    
