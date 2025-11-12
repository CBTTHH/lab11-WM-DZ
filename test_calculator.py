import unittest
from calculator import *

class TestCalculator(unittest.TestCase):


    def test_multiply(self):  # 3 assertions
        # Basic multiplication tests
        self.assertEqual(mul(5, 9), 45)
        self.assertEqual(mul(10, 7), 70)
        self.assertEqual(mul(0, 9), 0)


    def test_divide(self):  # 3 assertions
        self.assertAlmostEqual(div(10, 4), 2.5)
        self.assertEqual(div(90, 3), 30)



    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)


    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(-3, 4), 5.0)
        self.assertEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)

        self.assertEqual(square_root(16), 4.0)

        self.assertAlmostEqual(square_root(2), math.sqrt(2), places=6)

# Do not touch this
if __name__ == "__main__":
    unittest.main()