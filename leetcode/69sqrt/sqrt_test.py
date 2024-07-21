import unittest
from sqrt import sqrt 

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        x = 4
        expected = 2

        actual = sqrt(x)

        self.assertEqual(expected, actual)

    def test_example2(self):
        x = 8
        # rounded down
        expected = 2

        actual = sqrt(x)

        self.assertEqual(expected, actual)

    def test_example3(self):
        x = (2 ** 31) - 1
        # rounded down
        expected = 46340

        actual = sqrt(x)

        self.assertEqual(expected, actual)

    def test_example4(self):
        x = 0
        # rounded down
        expected = 0

        actual = sqrt(x)

        self.assertEqual(expected, actual)

