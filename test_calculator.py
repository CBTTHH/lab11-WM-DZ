# https://github.com/CBTTHH/lab11-WM-DZ.git
# Partner 1: William Munro
# Partner 2: David Zou


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 10), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(sub(11, 4), 7)
        self.assertEqual(sub(98, 99), -1)
        self.assertEqual(sub(11, -5), 16)
        self.assertEqual(sub(0, 4), -4)
        self.assertEqual(sub(11, 0), 11)

    def test_divide_by_zero(self):  # 1 assertion

        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(6, 3), 0.5)
        self.assertEqual(div(-10, 2), -0.2)
        self.assertAlmostEqual(div(5, 2), 0.4)


    def test_logarithm(self):  # 3 assertions
        self.assertEqual(round(log(5, 125)), 3)
        self.assertEqual(log(2, 32), 5)
        self.assertEqual(log(10, 10000), 4)
        self.assertEqual(log(2, 4), 2)
        self.assertEqual(log(10, 1), 0)


 
    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(10, -1)

        with self.assertRaises(ValueError):
            log(0, -3)

        with self.assertRaises(ValueError):
            log(100, 0)
            
    def test_log_invalid_argument(self):  # 1 assertion
        # log(x, base) — x must be > 0
        with self.assertRaises(ValueError):
            log(0, 10)
            
    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):  # 3 assertions
        # Invalid argument
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()