import unittest
from sum import threeSum 

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        data = [-1, 0, 1, 2, -1, -4]
        expected = [(-1, 0, 1), (-1,-1,2)]

        actual = threeSum(data)

        self.assertEqual(expected, actual)

    def test_example2(self):
        data = [-1]
        expected = []

        actual = threeSum(data)

        self.assertEqual(expected, actual)

    def test_example3(self):
        data = [0, 1, 1]
        expected = []

        actual = threeSum(data)

        self.assertEqual(expected, actual)
