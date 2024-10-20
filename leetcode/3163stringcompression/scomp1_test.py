import unittest
from scomp1 import compress

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        chars = "abcde"
        expected = "1a1b1c1d1e"
        actual = compress(chars)

        self.assertEqual(expected, actual)

    def test_example2(self):
        chars = "aaaaaaaaaaaaaabb"
        expected = "9a5a2b"
        actual = compress(chars)

        self.assertEqual(expected, actual)

