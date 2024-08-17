import unittest
from binsearch import binSearch 

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        testData = [1, 2, 3]

        target = 1
        expected = 0

        actual = binSearch(testData, target)

        self.assertEqual(expected, actual)


    def test_example3(self):
        testData = [3, 2, 1]

        target = 4444
        expected = -1

        actual = binSearch(testData, target)

        self.assertEqual(expected, actual)

    def test_example2(self):
        testData = [0, 0, 0, 0, 1, 2, 3, 10]

        target = 4444
        expected = -1

        actual = binSearch(testData, target)

        self.assertEqual(expected, actual)
