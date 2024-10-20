import unittest
from scomp import compress

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        expected = 6
        actual = compress(chars)

        self.assertEqual(expected, actual)

    def test_example2(self):
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        expected = 4
        actual = compress(chars)

        self.assertEqual(expected, actual)

    def test_example3(self):
        chars = ["a"]
        expected = 1
        actual = compress(chars)

        self.assertEqual(expected, actual)

    def test_example4(self):
        chars = ["a", "b", "c", "d", "e", "f", "g"]
        expected = 7
        actual = compress(chars)

        self.assertEqual(expected, actual)

    def test_example5(self):
        chars = ["a","a","a","b","b","a","a"]
        expected = 6
        actual = compress(chars)

        self.assertEqual(expected, actual)
