import unittest
import twonums

class SimpleTest(unittest.TestCase):
    def test_Equal1(self):
        given = [2, 11, 15, 7]
        target = 9

        expected = [0, 3]
        actual = twonums.findhashonepass(given, target)
        self.assertEqual(actual, expected)

    def test_Equal2(self):
        given = [3, 2, 4]
        target = 6 

        expected = [1, 2]
        actual = twonums.findhashonepass(given, target)
        self.assertEqual(actual, expected)

    def test_Equal3(self):
        given = [2, 11, 3, 7]
        target = 5

        expected = [0, 2]
        actual = twonums.findhashonepass(given, target)
        self.assertEqual(actual, expected)
