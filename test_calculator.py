import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(0,29), 29)
        self.assertEqual(add(31,2), 33)
        self.assertEqual(add(-10,100), 90)
        self.assertEqual(add(12,87), 99)
        self.assertEqual(add(11,0), 11)
        

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(11,4), 7)
        self.assertEqual(sub(98,99), -1)
        self.assertEqual(sub(11,-5), 16)
        self.assertEqual(sub(0,4), -4)
        self.assertEqual(sub(11,0), 11)


    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(5, 125), 3)
        self.assertEqual(log(2, 32), 5)
        self.assertEqual(log(10, 10000), 4)
        self.assertEqual(log(2, 4), 2)
        self.assertEqual(log(10, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)

        with self.assertRaises(ValueError):
            log(-3, 9)
        
        with self.assertRaises(ValueError):
            log(0, 100)
    
# Do not touch this
if __name__ == "__main__":
    unittest.main()