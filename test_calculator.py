import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

######### Partner 2
# def test_add(self): # 3 assertions
#     fill in code

# def test_subtract(self): # 3 assertions
#     fill in code
# ##########################

    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 10), 0)

# def test_divide(self): # 3 assertions
#     fill in code
# ##########################

######## Partner 2
# def test_divide_by_zero(self): # 1 assertion
#     # call division function inside, example:
#     # with self.assertRaises(<INSERT_ERROR_TYPE>):
#     #     div(0, 5)
#     fill in code
    def test_divide(self):  # 3 assertions
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(-10, 2), -5)
        self.assertAlmostEqual(div(5, 2), 2.5)
# def test_logarithm(self): # 3 assertions
#     fill in code

# def test_log_invalid_base(self): # 1 assertion
#     # use same technique from test_divide_by_zero
#     fill in code
# ##########################

######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        # log(x, base) — x must be > 0
        with self.assertRaises(ValueError):
            log(0, 10)
    #     # call log function inside, example:
#     # with self.assertRaises(<INSERT_ERROR_TYPE>):
#     #     logarithm(0, 5)
#     fill in code

# def test_hypotenuse(self): # 3 assertions
#     fill in code
    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

# def test_sqrt(self): # 3 assertions
#     # Test for invalid argument, example:
#     # with self.assertRaises(<INSERT_ERROR_TYPE>):
#     #    square_root(NUM)
#     # Test basic function
#     fill in code
##########################
    def test_sqrt(self):  # 3 assertions
        # Invalid argument
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()