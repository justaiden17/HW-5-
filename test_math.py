# test_math.py
# Name: Aiden Brown
# QCC ID: 24668959

import unittest
from my_math import abs_val, fibonacci, mean

class TestMyMath(unittest.TestCase):

    def test_abs_val_basic(self):
        self.assertEqual(abs_val(5), 5)
        self.assertEqual(abs_val(-5), 5)
        self.assertEqual(abs_val(0), 0)

    def test_abs_val_float(self):
        self.assertEqual(abs_val(-3.7), 3.7)
        self.assertEqual(abs_val(2.2), 2.2)
def test_abs_val_large_number(self):
    self.assertEqual(abs_val(-9999999), 9999999)

    def test_fibonacci_basic(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_bad_inputs(self):
        with self.assertRaises((TypeError, ValueError)):
            fibonacci(-1)

        with self.assertRaises((TypeError, ValueError)):
            fibonacci(3.5)

        with self.assertRaises((TypeError, ValueError)):
            fibonacci("7")

    def test_mean_basic(self):
        self.assertAlmostEqual(mean([1, 2, 3]), 2.0)
        self.assertAlmostEqual(mean([1.5, 2.5]), 2.0)
        self.assertAlmostEqual(mean([0, 0, 0, 0]), 0.0)

    def test_mean_singleton_and_mixed(self):
        self.assertAlmostEqual(mean([42]), 42.0)
        self.assertAlmostEqual(mean([1, 2.0, 3]), 2.0)

    def test_mean_errors(self):
        with self.assertRaises((ValueError, ZeroDivisionError)):
            mean([])

        with self.assertRaises((TypeError, ValueError)):
            mean([1, "two", 3])

if __name__ == "__main__":
    unittest.main(verbosity=2)