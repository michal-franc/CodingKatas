import unittest
from searchmatrix import searchMatrix

class BasicTestss(unittest.TestCase):
    def test_example1(self):

        testData = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        testTarget = 3

        actual = searchMatrix(testData, testTarget)
        expected = True

        self.assertEqual(expected, actual)
        
    def test_example2(self):

        testData = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        testTarget = 78

        actual = searchMatrix(testData, testTarget)
        expected = False

        self.assertEqual(expected, actual)

    def test_example3(self):

        testData = [[1]]
        testTarget = 2

        actual = searchMatrix(testData, testTarget)
        expected = False

        self.assertEqual(expected, actual)

    def test_example4(self):

        testData = [[1, 1]]
        testTarget = 2

        actual = searchMatrix(testData, testTarget)
        expected = False

        self.assertEqual(expected, actual)

    def test_example5(self):

        testData = [[1], [1]]
        testTarget = 2

        actual = searchMatrix(testData, testTarget)
        expected = False

        self.assertEqual(expected, actual)
