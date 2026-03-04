import unittest
import math
import sys
import os


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calculator import square_root, factorial, natural_log, power


class TestSquareRoot(unittest.TestCase):

    def test_perfect_square(self):
        self.assertAlmostEqual(square_root(9), 3.0)

    def test_zero(self):
        self.assertAlmostEqual(square_root(0), 0.0)

    def test_float(self):
        self.assertAlmostEqual(square_root(2), math.sqrt(2))

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            square_root(-1)


class TestFactorial(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_five(self):
        self.assertEqual(factorial(5), 120)

    def test_large(self):
        self.assertEqual(factorial(10), 3628800)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_float_raises(self):
        with self.assertRaises(ValueError):
            factorial(3.5)


class TestNaturalLog(unittest.TestCase):

    def test_one(self):
        self.assertAlmostEqual(natural_log(1), 0.0)

    def test_e(self):
        self.assertAlmostEqual(natural_log(math.e), 1.0)

    def test_positive(self):
        self.assertAlmostEqual(natural_log(10), math.log(10))

    def test_zero_raises(self):
        with self.assertRaises(ValueError):
            natural_log(0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            natural_log(-5)


class TestPower(unittest.TestCase):

    def test_square(self):
        self.assertAlmostEqual(power(2, 2), 4.0)

    def test_cube(self):
        self.assertAlmostEqual(power(3, 3), 27.0)

    def test_zero_exponent(self):
        self.assertAlmostEqual(power(5, 0), 1.0)

    def test_fractional_exponent(self):
        self.assertAlmostEqual(power(4, 0.5), 2.0)

    def test_negative_exponent(self):
        self.assertAlmostEqual(power(2, -1), 0.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
