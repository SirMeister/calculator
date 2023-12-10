import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 3), 9)

    # This test will fail
    def test_add_fail(self):
        self.assertEqual(self.calc.add(2, 2), 5)

    # This test will fail
    def test_subtract_fail(self):
        self.assertEqual(self.calc.subtract(5, 3), 1)

if __name__ == '__main__':
    unittest.main()