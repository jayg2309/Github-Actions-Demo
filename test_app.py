import unittest
from app import add

class TestAddFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -4), -6)

    def test_mixed_numbers(self):
        self.assertEqual(add(-3, 7), 4)

if __name__ == "__main__":
    unittest.main()
