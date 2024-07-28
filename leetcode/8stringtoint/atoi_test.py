import unittest
from atoi import atoi

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        data = "42"
        expected = 42

        actual = atoi(data)

        self.assertEqual(expected, actual)

    def test_example2(self):
        data = "-042"
        expected = -42

        actual = atoi(data)

        self.assertEqual(expected, actual)

    def test_example3(self):
        data = "-040"
        expected = -40

        actual = atoi(data)

        self.assertEqual(expected, actual)

    def test_example4(self):
        data = "-0"
        expected = 0

        actual = atoi(data)

        self.assertEqual(expected, actual)

    def test_example5(self):
        data = "-00000000000"
        expected = 0

        actual = atoi(data)

        self.assertEqual(expected, actual)

    def test_example6(self):
        data = "     -99"
        expected = -99

        actual = atoi(data)

        self.assertEqual(expected, actual)

    def test_example7(self):
        data = "1337c0d3"
        expected = 1337

        actual = atoi(data)

        self.assertEqual(expected, actual)

    def test_example8(self):
        data = "0-1"
        expected = 0 

        actual = atoi(data)

        self.assertEqual(expected, actual)

    def test_example9(self):
        data = "words ad 987"
        expected = 0 

        actual = atoi(data)

        self.assertEqual(expected, actual)

    def test_example10(self):
        data = "-91283472332"
        expected = -2147483648 

        actual = atoi(data)

        self.assertEqual(expected, actual)

    def test_example11(self):
        data = "+-12"
        expected = 0 

        actual = atoi(data)

        self.assertEqual(expected, actual)

    def test_example12(self):
        data = "21474836460"
        expected = 2147483647 

        actual = atoi(data)

        self.assertEqual(expected, actual)

    def test_example13(self):
        data = " + 413"
        expected = 0

        actual = atoi(data)

        self.assertEqual(expected, actual)

