import unittest
from validparent import isValid

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        x = "()"
        expected = True

        actual = isValid(x)

        self.assertEqual(expected, actual)


    def test_example2(self):
        x = "()[]{}"
        expected = True

        actual = isValid(x)

        self.assertEqual(expected, actual)

    def test_example3(self):
        x = "([{}])"
        expected = True

        actual = isValid(x)

        self.assertEqual(expected, actual)

    def test_example4(self):
        x = "([{})"
        expected = False

        actual = isValid(x)

        self.assertEqual(expected, actual)

    def test_example5(self):
        x = "("
        expected = False

        actual = isValid(x)

        self.assertEqual(expected, actual)

    def test_example6(self):
        x = "(("
        expected = False

        actual = isValid(x)

        self.assertEqual(expected, actual)

    def test_example7(self):
        x = "){"
        expected = False

        actual = isValid(x)

        self.assertEqual(expected, actual)

    def test_example8(self):
        x = ")({"
        expected = False

        actual = isValid(x)

        self.assertEqual(expected, actual)
