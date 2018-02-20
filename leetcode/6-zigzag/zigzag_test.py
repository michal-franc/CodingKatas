import unittest
from zigzag import convert

class SimpleTest(unittest.TestCase):
    def test_if_one_row_return_same_list(self):
        s = "TEST1TOTEST"
        actual = convert(s, 1)

        self.assertEquals(s, actual)

    def test_if_two_row_return_correct_result(self):
        s = "TESTMYTEST"
        expected = "TSMTSETYET"
        actual = convert(s, 2)

        self.assertEquals(expected, actual)

    def test_if_three_row_return_correct_result(self):
        s = "PAYPALISHIRING"
        expected = "PAHNAPLSIIGYIR"
        actual = convert(s, 3)

        self.assertEquals(expected, actual)

    def test_weird_case(self):
        s = "A"
        expected = "A"
        actual = convert(s, 2)

        self.assertEquals(expected, actual)
