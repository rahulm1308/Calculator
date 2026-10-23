import unittest
from calc import add, sub, mult, div


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)

    def test_mult(self):
        self.assertEqual(mult(10, 5), 50)

    def test_div(self):
        self.assertEqual(div(10, 5), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)


if __name__ == "__main__":
    unittest.main()
